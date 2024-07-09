from constants import tetromino_encoding


class TetroScriptTranslator():
    """
    Translator of TetroScript language.
    Takes in Parser result and runs the game.
    """

    # Instantiate variables
    def __init__(self):
        self.tetrominos = None
        self.gameboards = None
        self.controls = None
        self.games = None
        self.main = None

        self.game_config = dict()
        self.game_sequence = list()

    def translate(self, tetrominos, gameboards, controls, games, main):
        self.tetrominos = tetrominos
        self.gameboards = gameboards
        self.controls = controls
        self.games = games
        self.main = main

        for _, game in self.main:
            # Add game to sequence
            self.game_sequence.append(game)

            # Bad reference error : Game
            if game not in self.games:
                raise ReferenceError(f"Reference to {game} does not exist")

            # Store game config
            self.game_config[game] = dict()
            self.game_config[game]["blocks"] = list()
            self.game_config[game]["controls"] = list()

            # Attributes of the game
            game_attributes = self.games[game]

            for game_attribute in game_attributes:
                game_attribute_name, game_attribute_value = game_attribute

                # Handle case: Gameboard
                if game_attribute_name == "board":
                    # Bad reference error : Gameboard
                    if game_attribute_value not in self.gameboards:
                        raise ReferenceError(f"Reference to {game_attribute_value} does not exist")

                    board_attributes = self.gameboards[game_attribute_value]

                    # Add board attributes to game config
                    for board_attribute in board_attributes:
                        self.game_config[game][board_attribute[0]] = board_attribute[1]

                # Handle case: Levels
                if game_attribute_name == "levels":
                    # Add number of levels to game config
                    self.game_config[game]["levels"] = game_attribute_value

                # Handle case: Tetrominos
                if game_attribute_name == "blocks":
                    for tetromino in game_attribute_value:
                        # Bad reference: Tetromino
                        if tetromino not in self.tetrominos:
                            raise ReferenceError(f"Reference to {tetromino} does not exist")

                        tetromino_attributes = self.tetrominos[tetromino]

                        # Add tetromino info to game config
                        type_color = {"type": None, "color": -1}  # Default color = -1
                        for tetromino_attribute in tetromino_attributes:
                            if tetromino_attribute[0] == "type":
                                type_color["type"] = tetromino_encoding[tetromino_attribute[1]]

                            if tetromino_attribute[0] == "color":
                                type_color["color"] = tetromino_attribute[1]

                        # Bad Tetromino: All tetromino blocks need to have type
                        if type_color["type"] is None:
                            raise Exception(f"Tetromino {tetromino} doesn't have 'type' attribute specified")

                        self.game_config[game]["blocks"].append(type_color)

                # Handle case: Controls
                if game_attribute_name == "controls":

                    for control in game_attribute_value:
                        # Bad reference: Control
                        if control not in self.controls:
                            raise ReferenceError(f"Reference to {control} does not exist")

                        control_attributes = self.controls[control]

                        # Add control info to game config
                        key_action = {"key": None, "action": None}
                        for control_attribute in control_attributes:
                            if control_attribute[0] == "key":
                                key_action["key"] = control_attribute[1]

                            if control_attribute[0] == "action":
                                key_action["action"] = control_attribute[1]

                        # Every control needs to have key and action
                        if key_action["key"] is None or key_action["action"] is None:
                            raise Exception(f"Control {control} needs to have both 'key' and 'action'")

                        self.game_config[game]["controls"].append(key_action)

        # Game sequence
        return self.game_sequence, self.game_config
