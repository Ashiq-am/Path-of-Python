# Importing the Pygame library for game development
import pygame

# Importing the Time module for handling
# time-related operations
import time

# Initializing Pygame
pygame.init()

# Width of the game window
display_width = 800

# Height of the game window
display_height = 600

# Setting the display mode with specified width and height
display = pygame.display.set_mode((display_width,
								display_height))

# Updating the display
pygame.display.update()

# Setting the caption/title of the game window
pygame.display.set_caption("Car Game")

# Creating a Clock object to control game frame rate
clock = pygame.time.Clock()

# Flag to indicate if the car is bumped or not
bumped = False

# Looping until the car is bumped
while not bumped:
	# Checking for events (e.g. key presses, mouse clicks)
	for event in pygame.event.get():
		# If the QUIT event is triggered (user closes the game window)
		if event.type == pygame.QUIT:
			# Set the bumped flag to True to exit the game loop
			bumped = True
			# Quitting the game and closing the game window
			quit()
