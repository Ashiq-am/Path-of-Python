# Importing the library
import pygame

# Initializing Pygame
pygame.init()

# Creating the surface
sample_surface = pygame.display.set_mode((400, 300))

# changing the pixel format of an image
pygame.Surface.convert(sample_surface)

# updating the display
pygame.display.flip()
