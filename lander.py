# this module is a pygame lunar lander game

import pygame
import shapely
import sys
from pygame.locals import *
import random
import math

from consts import *
from geom import *
from images import *
from vectors import *
from drawutils import *
from entities import *
from states import *
from levelManager import *

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

game = PygameApp()
game.run()