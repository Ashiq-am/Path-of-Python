import pygame
import random

pygame.init()

# Dimensions of the screen
WIDTH, HEIGHT = 600, 500

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

font = pygame.font.Font('freesansbold.ttf', 15)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Breaker")

# to control the frame rate
clock = pygame.time.Clock()
FPS = 30
