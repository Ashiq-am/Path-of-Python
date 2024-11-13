# Importing the library
import pygame

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((400, 300))

# Initialing Color
color = (48, 141, 70)

# Drawing Rectangle
pygame.draw.rect(surface, color, pygame.Rect(
	30, 30, 60, 60), 2, border_bottom_right_radius=5)

# Displayig Object
pygame.display.flip()
