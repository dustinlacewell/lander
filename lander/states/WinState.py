import pygame
from pygame.locals import *

from .AppState import AppState
from lander.entities import Explosion

from lander.consts import *

class WinState(AppState):

    def __init__(self, app):
        super(WinState, self).__init__(app)
        app.levelManager.score += app.lander.fuel
        if app.levelManager.nextLevel():
            print(f"You won! Score: {app.levelManager.score}")
            exit()

    def handleKeys(self):
        keys = pygame.key.get_pressed()
        if any(keys):
            from .SetupState import SetupState
            self.app.setState(SetupState(self.app))

    def update(self):
        self.handleEvents()
        self.handleKeys()

    def drawLanding(self, _):
        super(WinState, self).drawLanding(True)