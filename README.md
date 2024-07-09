# Tetris Compiler by 2020B3A70541G

This project creates an interactive tetris games and offers the following features:

## Programmability Features

- Tetrominoes: x distinct tetrominoes are implemented.
- Style:
- Probability distribution:
- Game speed-up: Implemented using the DOWN arrow key. The speed-up of for the game can be given as an input.
- Levels: Implemented different levels of difficulty in the grammar.
- Scores: The score is updated every time a line in the game is filled. After the score update the line is deleted.
- Board Size: The dimension can be given as an input before running the game.

## File Descriptions

1. `constants.py` - has the required constants.
2. `tetris_game.py`- This is the complete game engine which builds the complete game.
3. `example1.txt` - This is the test file to parse and get the specifications for the game.
4. `helpers.py`- contains helper functions
5. `lexer.py` - Tokenizes the file to provide it to the parser.
6. `parser.py`- This parses through the test case file and obtains the specifications for the games.
7. `requirements.txt`- has the requirements
8. `testbench.py`- tests all the files
9. `translator.py`- translates.

## Instructions

In case the module pygame is not installed run the following command:

`pip install pygame`

Run the make file by running `make run` in the terminal.

Or alternatively type `python3 tetris_game.py`

## Acknowledgment

Contributions from Jibran, Ashray, Mohammed Aman.