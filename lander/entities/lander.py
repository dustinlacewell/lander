import math

import pygame

from lander.consts import *
from lander.images import *
from lander.drawutils import *


class Lander:
    def __init__(self, x, y, vx, vy, rotation):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.thrusting = False
        self.fuel = MAX_FUEL
        self.rotation = rotation
        self.lander_image = ArrayToPygameImage(LANDER)
        self.thrust_image = ArrayToPygameImage(LANDER_THRUSTING)

        # scale up lander images
        self.lander_image = pygame.transform.scale(self.lander_image, (self.lander_image.get_width() * 2, self.lander_image.get_height() * 2))
        self.thrust_image = pygame.transform.scale(self.thrust_image, (self.thrust_image.get_width() * 2, self.thrust_image.get_height() * 2))
        self.updateRect()

    def setPosition(self, x, y):
        self.x = x
        self.y = y
        self.updateRect()

    def setVelocity(self, vx, vy):
        self.vx = vx
        self.vy = vy

    def getVelocity(self):
        return math.sqrt(self.vx * self.vx + self.vy * self.vy)

    def updateRect(self):
        self.rect = pygame.Rect(
            self.x - self.lander_image.get_width() / 2,
            self.y - self.lander_image.get_height() / 2,
            self.lander_image.get_width(),
            self.lander_image.get_height() - 13)

    def draw(self, screen):
        image = self.thrust_image if self.thrusting and self.fuel else self.lander_image
        drawImageRotated(screen, image, -self.rotation, self.x, self.y)

    def turnLeft(self):
        self.rotation -= TURN_SPEED

    def turnRight(self):
        self.rotation += TURN_SPEED

    def update(self):
        offset = math.radians(90)
        if self.thrusting and self.fuel:
            self.fuel -= THRUST_COST
            self.vx -= THRUST_FORCE * math.cos(self.rotation + offset)
            self.vy -= THRUST_FORCE * math.sin(self.rotation + offset)

        self.x += self.vx
        self.y += self.vy
        self.vy += GRAVITY
        self.updateRect()
