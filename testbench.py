# ------------------------------------------------------------
# This file is testbench to test lexer, parser and translator's functionalities.
# ------------------------------------------------------------

from constants import EXAMPLE_1_PATH
from helpers import test_parser, test_lexer, test_translator
from lexer import TetroScriptLexer
from parser import TetroScriptParser
from translator import TetroScriptTranslator

if __name__ == "__main__":
    lexer = TetroScriptLexer()
    parser = TetroScriptParser()
    translator = TetroScriptTranslator()

    # test_lexer(lexer, EXAMPLE_1_PATH)
    # test_parser(parser, lexer, EXAMPLE_1_PATH)
    test_translator(translator, parser, lexer, EXAMPLE_1_PATH)
