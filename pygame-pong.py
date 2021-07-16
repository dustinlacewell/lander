# this module implements a pygame breakout game
# Author: lx
# Date: 2018-10-18
# Env: python 3.5
# Version: 1.0

import pygame
from random import *

def randomRGB():
    return randint(0, 255), randint(0, 255), randint(0, 255)

def calculateCollisionDirection(rect1, rect2):
    '''
    calculate the direction of collision
    returns 'up', 'down', 'left', 'right', 'none'
    '''
    if not rect1.colliderect(rect2):
        return 'none'

    if (rect1.y <= rect2.y - (rect2.w/2)):
        return 'down'

    if (rect1.y >= rect2.y + (rect2.w/2)):
        return 'up'

    if (rect1.x < rect2.x):
        return 'left'

    if (rect1.x > rect2.x):
        return 'right'


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

PADDLE_SPEED = 5
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
PADDLE_HALF_WIDTH = PADDLE_WIDTH // 2
PADDLE_HALF_HEIGHT = PADDLE_HEIGHT // 2
PADDLE_COLOR = (255, 255, 255)

PADDLE_X_RESET = SCREEN_WIDTH // 2
PADDLE_Y_RESET = SCREEN_HEIGHT - PADDLE_HEIGHT - 10

# ball is positioned centered, above the paddle
BALL_SPEED = 5
BALL_RADIUS = 10
BALL_DIAMETER = BALL_RADIUS * 2
BALL_COLOR = (255, 255, 255)
BALL_X_RESET = PADDLE_X_RESET
BALL_Y_RESET = PADDLE_Y_RESET + PADDLE_HALF_HEIGHT + BALL_RADIUS - 100

BLOCK_WIDTH = 20
BLOCK_HEIGHT = 20
BLOCK_ROWS = 8

# blocks are positioned at the top of the screen
BLOCKS_PER_ROW = SCREEN_WIDTH // BLOCK_WIDTH
BLOCKS_WIDTH = BLOCK_WIDTH * BLOCKS_PER_ROW
BLOCKS_MARGIN = (SCREEN_WIDTH - BLOCKS_WIDTH) // 2


class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = randomRGB()
        self.width = BLOCK_WIDTH
        self.height = BLOCK_HEIGHT
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


class BlockManager:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.blocks = []
        for i in range(BLOCK_ROWS):
            for j in range(BLOCKS_PER_ROW):
                self.blocks.append(Block(self.x + j * BLOCK_WIDTH, self.y + i * BLOCK_HEIGHT))

    def draw(self, screen):
        for block in self.blocks:
            block.draw(screen)

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = BALL_DIAMETER
        self.height = BALL_DIAMETER
        self.color = BALL_COLOR
        self.speed_x = BALL_SPEED
        self.speed_y = BALL_SPEED
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.width // 2)

    def reset(self):
        '''
        resets position centered above paddle position
        '''
        self.x = BALL_X_RESET
        self.y = BALL_Y_RESET

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.rect.x = self.x
        self.rect.y = self.y

    def bounce(self, direction):
        if direction == 'x':
            self.speed_x *= -1
        elif direction == 'y':
            self.speed_y *= -1

    def collide(self, rect):
        direction = calculateCollisionDirection(self.rect, rect)
        if direction != 'none':
            if direction == 'up':
                self.speed_y = abs(self.speed_y)
            elif direction == 'down':
                self.speed_y = -abs(self.speed_y)
            elif direction == 'left':
                self.speed_x = abs(self.speed_x)
            elif direction == 'right':
                self.speed_x = -abs(self.speed_x)
            return True
        return False


class Paddle:
    '''
    moves left and right
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.color = PADDLE_COLOR
        self.speed = PADDLE_SPEED
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def reset(self):
        self.x = PADDLE_X_RESET
        self.y = PADDLE_Y_RESET
        self.updateRect()

    def updateRect(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, direction):
        if direction == 'left':
            if self.x > 0:
                self.x -= self.speed
        elif direction == 'right':
            if self.x + self.width < SCREEN_WIDTH:
                self.x += self.speed
        self.updateRect()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.ball = Ball(BALL_X_RESET, BALL_Y_RESET)
        self.paddle = Paddle(PADDLE_X_RESET, PADDLE_Y_RESET)
        self.blockManager = BlockManager(BLOCKS_MARGIN, BLOCKS_MARGIN)

    def draw(self):
        self.screen.fill((0, 0, 0))
        # draw 1px border around screen in white
        pygame.draw.rect(self.screen, (255, 255, 255), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 1)

        self.ball.draw(self.screen)
        self.paddle.draw(self.screen)
        self.blockManager.draw(self.screen)
        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def check_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.paddle.move('left')
        elif keys[pygame.K_RIGHT]:
            self.paddle.move('right')

    def check_collisions(self):
        self.ball.collide(self.paddle.rect)

        for block in self.blockManager.blocks:
            if self.ball.collide(block.rect):
                self.blockManager.blocks.remove(block)

        # check if ball is out of bounds
        if self.ball.y >= SCREEN_HEIGHT - BALL_RADIUS:
            self.ball.bounce('y')
        elif self.ball.x >= SCREEN_WIDTH - BALL_RADIUS:
            self.ball.bounce('x')
        elif self.ball.x <= BALL_RADIUS:
            self.ball.bounce('x')
        elif self.ball.y <= BALL_RADIUS:
            self.ball.bounce('y')

    def update(self):
        self.check_events()
        self.check_keys()
        self.ball.update()
        self.check_collisions()

        # pump pygame events
        pygame.event.pump()

    def run(self):
        while True:
            self.update()
            self.draw()
            self.clock.tick(60)

game = Game()
game.run()