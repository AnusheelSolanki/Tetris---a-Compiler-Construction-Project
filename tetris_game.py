import pygame
import sys
from random import choice
import random
from lexer import TetroScriptLexer
from parser import TetroScriptParser

pygame.init()
pygame.font.init()

# Set up the font object
fontObj = pygame.font.Font(None, 26)  # Use default font and size 36


# Define colors for Tetrominos
COLORS = [
    (0, 0, 0),        # Black for empty space
    (255, 85, 85),    # Red
    (100, 200, 115),  # Green
    (120, 108, 245),  # Blue
    (255, 255, 85),   # Yellow
    (180, 105, 255),  # Purple
    (85, 255, 255),   # Cyan - for the I piece
    (255,192,203)     # Pink
]

# Define Tetromino shapes
TETRIS_SHAPES = {
    'T1': [(0, 0), (1, 0), (2, 0), (1, 1)],  
    'T2': [(0, 0), (1, 0), (0, 1), (1, 1)],  
    'T3': [(0, 1), (1, 1), (2, 1), (2, 0)],  
    'T4': [(0, 0), (0, 1), (1, 1), (1, 2)], 
    'T5': [(0, 1), (1, 1), (1, 0), (2, 0)],

}

def rotate_clockwise(shape):
    """Rotate the shape of the Tetromino clockwise"""
    return [(y, x) for x, y in shape]

# Tetromino class
class Tetromino:
    def __init__(self, shape, color, x=3, y=0):
        self.shape = shape
        self.color = color
        self.x = x
        self.y = y
        self.rotation = 0

    def rotate(self):
        self.shape = [(-y, x) for x, y in self.shape]  # Simple rotation formula

    def draw(self, surface):
        for x, y in self.shape:
            pygame.draw.rect(surface, COLORS[self.color], (30 * (self.x + x), 30 * (self.y + y), 30, 30))

class Tetris:
    rows = 20
    columns = 10

    def __init__(self):
        self.board = [[0 for _ in range(Tetris.columns)] for _ in range(Tetris.rows)]
        self.score = 0
        self.game_over = False
        self.current_piece = None
        self.next_piece = self.new_piece()

    def new_piece(self):
        shape = random.choice(list(TETRIS_SHAPES.values()))
        color = random.randint(1, len(COLORS) - 1)
        return Tetromino(shape, color)

    def spawn_piece(self):
        self.current_piece = self.next_piece
        self.next_piece = self.new_piece()
        if not self.valid_position(self.current_piece.shape, self.current_piece.x, self.current_piece.y):
            self.game_over = True

    def valid_position(self, shape, x, y):
        for (sx, sy) in shape:
            if x + sx < 0 or x + sx >= Tetris.columns or y + sy < 0 or y + sy >= Tetris.rows:
                return False
            if y + sy >= 0 and self.board[y + sy][x + sx] != 0:  
                return False
        return True

    def lock_piece(self):
        for (x, y) in self.current_piece.shape:
            if self.current_piece.y + y >= 0:  
                self.board[self.current_piece.y + y][self.current_piece.x + x] = self.current_piece.color
        self.clear_lines()
        self.spawn_piece()  

    def clear_lines(self):
        new_board = [row for row in self.board if 0 in row]
        cleared_lines = Tetris.rows - len(new_board)
        if cleared_lines > 0:
            self.score += cleared_lines * 10
            new_board = [[0 for _ in range(Tetris.columns)] for _ in range(cleared_lines)] + new_board
            self.board = new_board

    def move(self, dx, dy, rotate=False):
        if self.game_over:
            return
        x_new = self.current_piece.x + dx
        y_new = self.current_piece.y + dy
        new_shape = self.current_piece.shape if not rotate else rotate_clockwise(self.current_piece.shape)

        if self.valid_position(new_shape, x_new, y_new):
            self.current_piece.shape = new_shape
            self.current_piece.x = x_new
            self.current_piece.y = y_new
        elif dy > 0: 
            self.lock_piece()

    def draw(self, screen):
        screen.fill(COLORS[0]) 
        for y, row in enumerate(self.board):
            for x, cell_color in enumerate(row):
                if cell_color != 0:
                    pygame.draw.rect(screen, COLORS[cell_color], pygame.Rect(x * 30, y * 30, 30, 30))
        if self.current_piece:
            for x, y in self.current_piece.shape:
                pygame.draw.rect(screen, COLORS[self.current_piece.color], pygame.Rect((self.current_piece.x + x) * 30, (self.current_piece.y + y) * 30, 30, 30))

        
        score_text = fontObj.render(f'Score: {self.score}', True, (255, 255, 255))
        screen.blit(score_text, (screen.get_width() - 150, 20))

# Gameboard class
class Gameboard:
    def __init__(self, width, height, tetrominos):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.tetrominos = tetrominos
        self.current_tetromino = choice(tetrominos)  

    def update(self):
        
        self.current_tetromino.y += 1

    def draw(self, surface):
        for row in self.grid:
            for cell in row:
                color = COLORS[cell]
                pygame.draw.rect(surface, color, pygame.Rect(cell * 30, cell * 30, 30, 30))
        self.current_tetromino.draw(surface)


def parse_config(filename):
    lexer = TetroScriptLexer()
    parser = TetroScriptParser()
    with open(filename, 'r') as file:
        text = file.read()


    parsed_data = parser.parse(lexer.tokenize(text))
    tetrominos, gameboards, controls, games, main = parsed_data


    tetros = list()
    gameboards_list = list()
    games_list = list()
    control_list = list()
    main_list = list()
    for _,properties in tetrominos.items():
        tetros = properties
    for _,properties in gameboards.items():
        games_list = properties
    for _,properties in controls.items():
        control_list = properties
    for _,properties in games.items():
        games_list = properties


    config_dict = {
        'tetrominos': [{tup[0]:tup[1]} for tup in tetros],
        'gameboards': [{tup[0]:tup[1]} for tup in gameboards_list],
        'controls': [{tup[0]:tup[1]} for tup in control_list],
        'games': [{tup[0]:tup[1]} for tup in games_list],
        'main': [{tup[0]:tup[1]} for tup in main],
    }

    return config_dict


# Function to run the game
def run_game(width, height):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    tetris = Tetris()
    tetris.spawn_piece()

    key_actions = {
        'UP': lambda: tetris.move(0, 0, True),
        'DOWN': lambda: tetris.move(0, 1),
        'LEFT': lambda: tetris.move(-1, 0),
        'RIGHT': lambda: tetris.move(1, 0)
    }

    running = True
    while running:
        if tetris.game_over:
            print(f"Game Over! Your score was: {tetris.score}")
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                for key in key_actions:
                    if event.key == getattr(pygame, f'K_{key}'):
                        key_actions[key]()

        tetris.move(0, 1)  # Automatically move down
        screen.fill(COLORS[0])
        tetris.draw(screen)
        pygame.display.flip()
        clock.tick(2)  # Slow down game speed for testing

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    config_data = parse_config('example1.txt')  # Ensure you have this file
    print(config_data)
    run_game(300,600)
