import pygame
from pygame.locals import *

from .AppState import AppState
from .LoseState import LoseState
from .WinState import WinState
from lander.consts import *

class GameState(AppState):

    def handleKeys(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.app.lander.turnLeft()
        elif keys[K_RIGHT]:
            self.app.lander.turnRight()
        if keys[K_SPACE]:
            self.app.lander.thrusting = True
        else:
            self.app.lander.thrusting = False

    def update(self):
        super(GameState, self).update()
        self.checkEndConditions()
        condition = self.checkEndConditions()

        if condition == True:
            self.app.setState(LoseState(self.app))
        elif condition == False:
            self.app.setState(WinState(self.app))

