from consts import *
from images import *


class Explosion:
    def __init__(self, x, y):
        self.setupImages()
        self.setPosition(x, y)

    def setupImages(self):
        self.image = ArrayToPygameImage(EXPLOSION)
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.image.set_colorkey((0, 0, 0))
        self.rect = pygame.rect.Rect(0, 0, 64, 64)

    def setPosition(self, x, y):
        self.x = x
        self.y = y
        self.rect.center = (x + 16, y + 16)

    def draw(self, screen):
        screen.blit(self.image, self.rect)