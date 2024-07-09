from sly import Lexer


class TetroScriptLexer(Lexer):
    """
    Defines the functionality of Lexer used by TetroScript Language.
    Scans input string and creates tokens.
    Tokens are then further used by Parser for further stages of compilation.
    """

    # Represent a set of legal tokens.
    tokens = {
        # Generic tokens
        TOK_NUMBER,
        TOK_ID,
        TOK_TYPE_OPTION,
    }

    # White space between tokens is ignored by the scanner.
    ignore = " \t"

    # Ignore comments
    ignore_comment = r'\#.*'

    # Punctuation literals are converted into tokens with type same as value.
    # Example: "=" is converted to Token(type="=", value="=").
    literals = {
        "=",
        "{",
        "}",
        "[",
        "]",
        ",",
        ";"
    }

    # Reserved keywords
    # Define value:token dictionary
    reserved_keywords = {
        "gameboard": "TOK_GAMEBOARD",
        "x_size": "TOK_X_SIZE",
        "y_size": "TOK_Y_SIZE",
        "falling_speed": "FALLING_SPEED",
        "tetromino": "TOK_TETROMINO",
        "type": "TOK_TYPE",
        "color": "TOK_COLOR",
        "control": "TOK_CONTROL",
        "key": "TOK_KEY",
        "action": "TOK_ACTION",
        "game": "TOK_GAME",
        "board": "TOK_BOARD",
        "blocks": "TOK_BLOCKS",
        "levels": "TOK_LEVELS",
        "controls": "TOK_CONTROLS",
        "main": "TOK_MAIN",
        "play": "TOK_PLAY",
    }

    # Update tokens set to include reserved keyword tokens too.
    tokens = tokens.union(reserved_keywords.values())

    # Regex for matching token type option
    # User has 7 options: T1, T2, T3, T4, T5, T6, T7
    TOK_TYPE_OPTION = r"T[1-7]"

    @_(r'[a-z][a-z0-9_]*')
    def TOK_ID(self, t):
        """
        Regex for matching TOK_ID.
        TOK_ID can start with lowercase letter followed by any number of
        lowercase letter, digits or underscores.
        """
        # If lexicon is reserved keyword, return appropriate token.
        t.type = self.reserved_keywords.get(t.value, 'TOK_ID')
        return t

    @_(r'\d+')
    def TOK_NUMBER(self, t):
        """
        Regex to match TOK_NUMBER
        Converts the string to integer (number) before returning.
        """
        t.value = int(t.value)
        return t

    # Define a rule so we can track line numbers
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)
        pass  # Basically ignore new line

    def error(self, t):
        """
        Handle error, incase an illegal character is encountered.
        """
        print(f"ERROR: An illegal character {t.value[0]} in {self.lineno}.")
        self.index += 1  # Move ahead one character
