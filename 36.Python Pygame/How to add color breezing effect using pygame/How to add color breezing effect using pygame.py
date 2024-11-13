import pygame
import random
import sys

# initializing the constructor
pygame.init()

# setting up variable screen
screen = pygame.display.set_mode((720, 720))

# three arguments of the color tuple
c1 = random.randint(0, 255)
c2 = random.randint(0, 255)
c3 = random.randint(0, 255)

# setting up variable clock
clock = pygame.time.Clock()

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()

    # increases the shade of
    # the current color
    if 0 < c1 < 255:
        c1 += 1

    # if value of c1 exceeds
    # 255 it resets it to 0
    elif c1 >= 255:
        c1 -= 255

    # if value of c1 preceeds 0
    # it is increamented by 3
    elif c1 <= 0:
        c1 += 3

    # sets game fps to 60
    clock.tick(60)

    # sets bg color to tuple
    # (c1,c2,c3)
    screen.fill((c1, c2, c3))

    # updates the frames of
    # the game
    pygame.display.update()
