from lander.consts import *
from lander.images import *


class LandingPlatform:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.setupImages()
        self.updateRect()

    def setupImages(self):
        self.image = ArrayToPygameImage(PLATFORM)
        self.active_image = ArrayToPygameImage(PLATFORM, (255, 0, 255))
        self.image = pygame.transform.scale(self.image, (64, 32))
        self.active_image = pygame.transform.scale(self.active_image, (64, 32))

    def update(self):
        self.updateRect()

    def updateRect(self):
        w = self.image.get_width()
        h = self.image.get_height()

        self.rect = pygame.Rect(
            self.x - w / 2,
            self.y - h / 2,
            w, h)

        self.landing_rect = pygame.Rect(
            self.x - w / 2,
            self.y - h / 2 - h,
            w, h*2)

    def draw(self, screen, active=False):
        image = self.active_image if active else self.image
        screen.blit(image, self.rect)
        # draw self.rect
        # pygame.draw.rect(screen, (255, 0, 0), self.rect, 1)
        # draw self.landing_rect
        # pygame.draw.rect(screen, (0, 255, 0), self.landing_rect, 1)

    def readyForApproach(self, rect):
        return self.landing_rect.colliderect(rect)

    def collidesWith(self, rect):
        return self.rect.colliderect(rect)