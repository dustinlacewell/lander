import math
import random

from lander.consts import *

from .AppState import AppState
from .GameState import GameState

from lander.entities import *



class SetupState(AppState):

    def __init__(self, app):
        super(SetupState, self).__init__(app)
        self.createGuage()
        self.createTerrain()
        self.createLandingPlatform()
        self.createLander()

    def randomizeLander(self):
        x = random.randint(30, SCREEN_WIDTH - 30)
        y = random.randint(30, 200)
        self.app.lander.setPosition(x, y)

    def createLander(self):
        vx = random.randint(-2, 2)
        vy = random.randint(-2, 0)
        r = random.randint(-45, 45)
        self.app.lander = Lander(0, 0, vx, vy, math.radians(r))
        self.randomizeLander()
        while self.checkEndConditions():
            self.randomizeLander()


    def createGuage(self):
        self.app.guage = FuelGauge(10, 10, 40, SCREEN_HEIGHT * 0.3)

    def createTerrain(self):
        levelConfig = self.app.levelManager.getConfig()
        self.app.terrain = Terrain(*levelConfig)

    def createLandingPlatform(self):
        index = random.randint(3, len(self.app.terrain.lines) - 3)
        p1, p2 = self.app.terrain.lines[index]
        x = p1[0]
        segs, vary, size = self.app.levelManager.getConfig()
        y = random.randint(SCREEN_HEIGHT - 16 - size, SCREEN_HEIGHT - 16)
        self.app.platform = LandingPlatform(x, y)
        y += 16

        width = 4

        for i in range(len(self.app.terrain.lines)):
            p1, p2 = self.app.terrain.lines[i]
            x1, y1 = p1
            x2, y2 = p2

            if i < index - width or i > index + width:
                continue

            if i == index - width:
                self.app.terrain.lines[i] = (
                    (x1, y1),
                    (x2, y),
                )
            elif i == index + width:
                self.app.terrain.lines[i] = (
                    (x1, y),
                    (x2, y2),
                )
            elif i > index - width and i < index + width:
                self.app.terrain.lines[i] = (
                    (x1, y),
                    (x2, y),
                )


    def update(self):
        self.app.setState(GameState(self.app))