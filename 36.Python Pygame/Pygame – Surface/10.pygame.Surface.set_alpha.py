# Importing the library
import pygame

# Initializing Pygame
pygame.init()

# creating the display surface
display_surface = pygame.display.set_mode((500, 500 ))

# Creating the image surface
image = pygame.image.load('gfg_logo.png')

# puting our image surface on display surface
# making the alpha value of surface as 100
pygame.Surface.set_alpha(image, 100)

display_surface.blit(image,(100,100))

# updating the display
pygame.display.flip()
