# ------------------------------------------------------------
# This file contains constants used throughout the project.
# ------------------------------------------------------------

import os

CURR_DIR = os.path.dirname(os.path.abspath(__file__))

EXAMPLE_1_PATH = os.path.join(CURR_DIR, "examples", "example1.txt")

tetromino_encoding = {
    "T1": 0,
    "T2": 1,
    "T3": 2,
    "T4": 3,
    "T5": 4,
    "T6": 5,
    "T7": 6,
}