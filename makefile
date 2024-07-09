# Makefile for Tetris game

# Compiler
PYTHON = python3

# Flags
PYFLAGS = -m py_compile

# Targets
all: compile run

compile:
	$(PYTHON) $(PYFLAGS) tetris_game.py

run:
	$(PYTHON) tetris_game.py

clean:
	rm -rf __pycache__

.PHONY: all compile run clean
