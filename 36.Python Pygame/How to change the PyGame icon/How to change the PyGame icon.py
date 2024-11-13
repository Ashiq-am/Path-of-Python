# Python program to change
# the Pygame icon

# Import the library Pygame
import pygame

# Construct the GUI game
pygame.init()

# Set dimensions of game GUI
screen = pygame.display.set_mode([600, 400])

# Take image as input
img = pygame.image.load('gfg_image.jpg')

# Set image as icon
pygame.display.set_icon(img)

# Set running value
running = True

# Setting what happens when game
# is in running state
while running:
	for event in pygame.event.get():

		# Close if the user quits the game
		if event.type == pygame.QUIT:
			running = False

	# Set the background color
	screen.fill((255, 255, 0))

	# Draw a circle on the screen
	pygame.draw.circle(screen, (0, 0, 0), (300, 200), 75)

	# Update the GUI game
	pygame.display.update()

# Quit the GUI game
pygame.quit()
