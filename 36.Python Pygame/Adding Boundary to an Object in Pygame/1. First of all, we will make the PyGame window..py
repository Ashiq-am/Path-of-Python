# importing the module
import pygame

# instantiating the class
pygame.init()

# dimension of the screen
width = 700
height = 550

# colours
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# creating a Screen
screen = pygame.display.set_mode((width, height))

# title of the screen
pygame.display.set_caption("Bouncy Ball")
