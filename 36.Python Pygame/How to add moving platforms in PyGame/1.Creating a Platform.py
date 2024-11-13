# Importing the pygame module
import pygame
from pygame.locals import *

# Initiate pygame and give permission
# to use pygame's functanility
pygame.init()

# Create a display surface object
# of specific dimension
window = pygame.display.set_mode((600, 600))

# Creating a new clock object to
# track the amount of time
clock = pygame.time.Clock()

# Starting coordinates of the platform
x = 100
y = 150

# Creating a rect with width
# and height
rect = Rect(x, y, 200, 50)

# Creating a boolean variable that
# we will use to run the while loop
run = True

# Creating an infinite loop
# to run our game
while run:
    # Setting the framerate to 30fps
    clock.tick(30)

    # Drawing the rect on the screen using the
    # draw.rect() method
    pygame.draw.rect(window, (255, 0, 0), rect)

    # Updating the display surface
    pygame.display.update()

    # Filling the window with white color
    window.fill((255, 255, 255))
