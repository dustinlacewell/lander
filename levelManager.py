from consts import *

LEVELS = [
    # segments, variation, size
    (10, 5, 10),
    (10, 5, 30),
    (50, 20, 80),
    (50, 30, 150),
    (50, 30, 250),
    (100, 30, 350),
    (100, 100, 300),
]

class LevelManager:
    def __init__(self):
        self.level = 0
        self.score = 0

    def getConfig(self):
        return LEVELS[self.level]

    def nextLevel(self):
        self.level += 1
        if self.level == len(LEVELS):
            return True

    def reset(self):
        self.level = 0
        self.score = 0
