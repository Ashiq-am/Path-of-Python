# Importing the library
import pygame

# Initializing Pygame
pygame.init()

# creating the display surface
display_surface = pygame.display.set_mode((500, 500 ))

# Creating the first image surface
image1 = pygame.image.load('gfg_logo.png')

# Creating the second image surface
image2 = pygame.image.load('gfg_logo.png')

# puting our first image surface on
# display surface
display_surface.blit(image1,(0,0))

# puting our second image surface on
# display surface
display_surface.blit(image1,(300,300))

# updating the display
pygame.display.flip()
