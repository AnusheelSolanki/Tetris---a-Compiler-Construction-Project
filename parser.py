from sly import Parser

from lexer import TetroScriptLexer


class TetroScriptParser(Parser):
    """
    Defines a parser for TetroScript language.
    Creates a parser using the TetroScript Grammar.
    The parser then parses the tokens fed by Lexer.
    """

    # Set of token defined in lexer
    tokens = TetroScriptLexer.tokens

    def __init__(self, *, debug=False):
        self.debug = debug
        self.tetrominos = dict()
        self.gameboards = dict()
        self.controls = dict()
        self.games = dict()
        self.main = []

    @_(
        'S'
    )
    def S_0(self, p):
        if self.debug:
            # print("Debug Logger S_0:", p[0])
            print("Parsed Tetrominos:", self.tetrominos)
            print("Parsed Gameboards:", self.gameboards)
            print("Parsed Controls:", self.controls)
            print("Parsed Games:", self.games)
            print("Parsed Main:", self.main)

        return self.tetrominos, self.gameboards, self.controls, self.games, self.main

    @_(
        'TETROMINO S',
        'GAMEBOARD S',
        'CONTROL S',
        'GAME S',
        'MAIN'
    )
    def S(self, p):
        # if self.debug:
        #     print("Debug logger S:", p[0])
        pass

    @_(
        'TOK_TETROMINO TOK_ID "{" TETROMINO_ATTRIBUTES "}"'
    )
    def TETROMINO(self, p):
        if self.debug:
            print("Debug logger TETROMINO:", p[0], p[1], p[3])

        self.tetrominos[p[1]] = p[3]

    @_(
        'TETROMINO_ATTRIBUTE TETROMINO_ATTRIBUTES'
    )
    def TETROMINO_ATTRIBUTES(self, p):
        if self.debug:
            print("Debug logger TETROMINO_ATTRIBUTES Type 2:", p[0], p[1])
        return [p[0], *p[1]]

    @_(
        'TETROMINO_ATTRIBUTE'
    )
    def TETROMINO_ATTRIBUTES(self, p):
        if self.debug:
            print("Debug logger TETROMINO_ATTRIBUTES Type 1:", p[0])
        return [p[0]]

    @_(
        'TOK_TYPE "=" TOK_TYPE_OPTION ";"',
        'TOK_COLOR "=" TOK_NUMBER ";"',
    )
    def TETROMINO_ATTRIBUTE(self, p):
        if self.debug:
            print("Debug logger TETROMINO_ATTRIBUTE:", p[0], p[2])
        return p[0], p[2]

    @_(
        'TOK_GAMEBOARD TOK_ID "{" GAMEBOARD_ATTRIBUTES "}"'
    )
    def GAMEBOARD(self, p):
        if self.debug:
            print("Debug logger GAMEBOARD:", p[0], p[1], p[3])

        self.gameboards[p[1]] = p[3]

    @_(
        'GAMEBOARD_ATTRIBUTE GAMEBOARD_ATTRIBUTES'
    )
    def GAMEBOARD_ATTRIBUTES(self, p):
        if self.debug:
            print("Debug logger GAMEBOARD_ATTRIBUTES Type 2:", p[0], p[1])
        return [p[0], *p[1]]

    @_(
        'GAMEBOARD_ATTRIBUTE'
    )
    def GAMEBOARD_ATTRIBUTES(self, p):
        if self.debug:
            print("Debug logger GAMEBOARD_ATTRIBUTES Type 1:", p[0])
        return [p[0]]

    @_(
        'TOK_X_SIZE "=" TOK_NUMBER ";"',
        'TOK_Y_SIZE "=" TOK_NUMBER ";"',
        'FALLING_SPEED "=" TOK_NUMBER ";"',
    )
    def GAMEBOARD_ATTRIBUTE(self, p):
        if self.debug:
            print("Debug logger GAMEBOARD_ATTRIBUTE:", p[0], p[2])
        return p[0], p[2]

    @_(
        'TOK_CONTROL TOK_ID "{" CONTROL_ATTRIBUTES "}"'
    )
    def CONTROL(self, p):
        if self.debug:
            print("Debug logger CONTROL:", p[0], p[1], p[3])

        self.controls[p[1]] = p[3]

    @_(
        'CONTROL_ATTRIBUTE CONTROL_ATTRIBUTES'
    )
    def CONTROL_ATTRIBUTES(self, p):
        if self.debug:
            print("Debug logger CONTROL_ATTRIBUTES Type 2:", p[0], p[1])
        return [p[0], *p[1]]

    @_(
        'CONTROL_ATTRIBUTE'
    )
    def CONTROL_ATTRIBUTES(self, p):
        if self.debug:
            print("Debug logger CONTROL_ATTRIBUTES Type 1:", p[0])
        return [p[0]]

    @_(
        'TOK_KEY "=" TOK_NUMBER ";"',
        'TOK_ACTION "=" TOK_NUMBER ";"',
    )
    def CONTROL_ATTRIBUTE(self, p):
        if self.debug:
            print("Debug logger CONTROL_ATTRIBUTE:", p[0], p[2])
        return p[0], p[2]

    @_(
        'TOK_GAME TOK_ID "{" GAME_ATTRIBUTES "}"'
    )
    def GAME(self, p):
        if self.debug:
            print("Debug logger GAME:", p[0], p[1], p[3])

        self.games[p[1]] = p[3]

    @_(
        'GAME_ATTRIBUTE GAME_ATTRIBUTES'
    )
    def GAME_ATTRIBUTES(self, p):
        if self.debug:
            print("Debug logger GAME_ATTRIBUTES Type 2:", p[0], p[1])
        return [p[0], *p[1]]

    @_(
        'GAME_ATTRIBUTE'
    )
    def GAME_ATTRIBUTES(self, p):
        if self.debug:
            print("Debug logger GAME_ATTRIBUTES Type 1:", p[0])
        return [p[0]]

    @_(
        'TOK_BOARD "=" TOK_ID ";"',
        'TOK_LEVELS "=" TOK_NUMBER ";"',
        'TOK_BLOCKS "=" ARRAY ";"',
        'TOK_CONTROLS "=" ARRAY ";"',
    )
    def GAME_ATTRIBUTE(self, p):
        if self.debug:
            print("Debug logger GAME_ATTRIBUTE:", p[0], p[2])
        return p[0], p[2]

    @_(
        '"[" IDS',
    )
    def ARRAY(self, p):
        if self.debug:
            print("Debug logger ARRAY:", p[1])
        return p[1]

    @_(
        'TOK_ID "," IDS',
    )
    def IDS(self, p):
        if self.debug:
            print("Debug logger IDS Type 2:", p[0], p[1], p[2])
        return [p[0], *p[2]]

    @_(
        'TOK_ID "]"',
    )
    def IDS(self, p):
        if self.debug:
            print("Debug logger IDS Type 1:", p[0])
        return [p[0]]

    @_(
        'TOK_MAIN "{" MAIN_ATTRIBUTES "}"'
    )
    def MAIN(self, p):
        if self.debug:
            print("Debug logger MAIN:", p[0], p[2])

        self.main.extend(p[2])

    @_(
        'MAIN_ATTRIBUTE MAIN_ATTRIBUTES'
    )
    def MAIN_ATTRIBUTES(self, p):
        if self.debug:
            print("Debug logger MAIN_ATTRIBUTES Type 2:", p[0], p[1])
        return [p[0], *p[1]]

    @_(
        'MAIN_ATTRIBUTE'
    )
    def MAIN_ATTRIBUTES(self, p):
        if self.debug:
            print("Debug logger MAIN_ATTRIBUTES Type 1:", p[0])
        return [p[0]]

    @_(
        'TOK_PLAY TOK_ID ";"',
    )
    def MAIN_ATTRIBUTE(self, p):
        if self.debug:
            print("Debug logger MAIN_ATTRIBUTE:", p[0], p[2])
        return p[0], p[1]
