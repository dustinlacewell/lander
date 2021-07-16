import math
import pygame


def drawLine(screen, p1, p2, color=(255, 255, 255)):
    pygame.draw.line(screen, color, p1, p2)

def drawImageRotated(surface, image, radians, x, y):
    """
    Draws a pygame image with rotation.
    """
    rotatedImage = pygame.transform.rotate(image, math.degrees(radians))
    rect = rotatedImage.get_rect()
    rect.center = (x, y)
    surface.blit(rotatedImage, rect)

def drawLines(screen, lines):
    for line in lines:
        pygame.draw.line(screen, (255, 255, 255), line[0], line[1], 1)

def drawText(screen, text, x, y, color=(255, 255, 255)):
    font = pygame.font.Font(None, 36)
    text = font.render(text, 1, color)
    textpos = text.get_rect()
    textpos.left = x
    textpos.top = y
    screen.blit(text, textpos)

