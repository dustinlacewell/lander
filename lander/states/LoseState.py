import pygame
from pygame.locals import *

from .AppState import AppState
from lander.entities import Explosion

from lander.consts import *

class LoseState(AppState):

    def __init__(self, app):
        super(LoseState, self).__init__(app)
        self.app.levelManager.reset()
        self.explosion = Explosion(app.lander.rect.x, app.lander.rect.y)

    def handleKeys(self):
        keys = pygame.key.get_pressed()
        if any(keys):
            from .SetupState import SetupState
            self.app.setState(SetupState(self.app))

    def update(self):
        self.handleEvents()
        self.handleKeys()

    def draw(self):
        super(LoseState, self).draw()
        if self.explosion:
            self.explosion.draw(self.app.screen)
