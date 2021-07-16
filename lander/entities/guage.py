import pygame

class FuelGauge:
    '''a vertical fuel guage with a border drawn with rects'''
    def __init__(self, top, left, width, height):
        self.top = top
        self.left = left
        self.width = width
        self.height = height

    def draw(self, surface, fuel):
        fuel = min(fuel, 1.0)
        # draw border
        pygame.draw.rect(surface, (255, 255, 255), (self.left, self.top, self.width, self.height), 1)
        # draw fuel level
        # pygame.draw.rect(surface, (255, 0, 0), (self.left + 1, self.top + 1, self.width - 2, self.height - 2), 0)
        height = (self.height - 2) * fuel
        pygame.draw.rect(surface, (255, 255, 255), (self.left + 1, self.top + (self.height - height), self.width - 2, height))

