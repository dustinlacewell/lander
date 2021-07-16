# this module is a pygame lunar lander game

import pygame
import shapely
import sys
from pygame.locals import *
import random
import math

from lander.consts import *
from lander.geom import *
from lander.images import *
from lander.vectors import *
from lander.drawutils import *
from lander.entities import *
from lander.states import *
from lander.levelManager import *

class PygameApp:
    def __init__(self):
        self.running = True
        self.setupPygame()
        self.levelManager = LevelManager()
        self.setState(SetupState(self))

    def setupPygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

    def setState(self, state):
        self.state = state

    def run(self):
        while self.running:
            self.state._update()
            self.state._draw()

def main():
    game = PygameApp()
    game.run()
