import pygame

from consts import *
from drawutils import *
from geom import *
from entities import *

class AppState:
    """
    This class is used to store the application state.
    """

    def __init__(self, app):
        self.app = app

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.running = False

    def handleKeys(self):
        pass

    def landerSafeSpeed(self):
        return self.app.lander.getVelocity() <= MAX_VELOCITY

    def landerApproaching(self):
        return self.app.platform.readyForApproach(self.app.lander.rect)

    def landerTouching(self):
        return self.app.platform.collidesWith(self.app.lander.rect)

    def landerCrashed(self):
        return self.app.terrain.intersectsRect(self.app.lander.rect)

    def drawScore(self):
        fuel = self.app.lander.fuel
        drawText(self.app.screen, f"Score: {self.app.levelManager.score}", 70, 10)

    def drawVelocity(self):
        velocity = self.app.lander.getVelocity()
        drawText(self.app.screen, f"Velocity: {velocity:.2f}", 70, 40)

    def drawGuage(self):
        self.app.guage.draw(self.app.screen, self.app.lander.fuel / MAX_FUEL)

    def drawTerrain(self):
        drawLines(self.app.screen, self.app.terrain.lines)

    def drawLander(self):
        self.app.lander.draw(self.app.screen)

    def drawLanding(self, approaching):
        self.app.platform.draw(self.app.screen, approaching)

    def drawBorder(self):
        pygame.draw.rect(self.app.screen, (255, 255, 255), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 1)

    def updateLander(self):
        self.app.lander.update()

    def updateLanding(self):
        self.app.platform.update()

    def draw(self):
        self.app.screen.fill((0, 0, 0))
        self.drawLander()
        self.drawScore()
        self.drawVelocity()
        self.drawGuage()
        self.drawTerrain()
        self.drawLanding(False)
        self.drawBorder()

    def _draw(self):
        self.draw()
        pygame.display.flip()

    def update(self):
        self.handleEvents()
        self.handleKeys()
        self.updateLander()
        self.updateLanding()

    def _update(self):
        self.update()
        self.app.clock.tick(30)

    def checkLanderOffscreen(self):
        offscreen = self.app.lander.rect.right < 0
        offscreen = offscreen or self.app.lander.rect.left > SCREEN_WIDTH
        offscreen = offscreen or self.app.lander.rect.top > SCREEN_HEIGHT
        return offscreen

    def checkEndConditions(self):
        if self.landerTouching():
            if self.landerSafeSpeed():
                return False
            else:
                print(f"Crashed into platform at {self.app.lander.rect.x}.")
                return True

        elif self.landerCrashed():
            print(f"Crashed into the ground at {self.app.lander.rect.x}.")
            return True

        elif self.checkLanderOffscreen():
            print(f"Lander wandered off.")
            return True