# Importing the library
import pygame

# Initializing Pygame
pygame.init()

# Creating the surface
sample_surface = pygame.display.set_mode((400, 300))

# creating a copy of sample_surface
# and naming it as copied_surface
copied_surface = pygame.Surface.copy(sample_surface)

# updating the display
pygame.display.flip()
