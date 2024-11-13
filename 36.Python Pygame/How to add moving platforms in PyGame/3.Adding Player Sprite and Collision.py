# Importing the pygame module
import pygame
from pygame.locals import *

# Initiate pygame and give permission
# to use pygame's functanility
pygame.init()

# Create a display surface object
# of specific dimension
window = pygame.display.set_mode((600,600))

# Creating a new clock object to
# track the amount of time
clock = pygame.time.Clock()

# Variable to store the
# velocity of the platform
platform_vel = 5

# Starting coordinates of the platform
x = 100
y = 150

# Starting coordinates for
# player sprite
player_x = 180
player_y = 0

# Creating a new variable
# for gravity
gravity = 8

# Creting a new rect for player
player_rect = Rect(player_x, player_y, 50, 50)

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

	# Multiplying platform_vel with -1
	# if its x coordinate is less then 100
	# or greater than or equal to 300.
	if rect.left >=300 or rect.left<100:
		platform_vel*= -1

	# Checking if player is colliding
	# with platform or not using the
	# colliderect() method.
	# It will return a boolean value
	collide = pygame.Rect.colliderect(rect, player_rect)

	# If player is colliding with
	# platform then setting coordinate
	# of player botton equal to top of platorm
	# and adding the platform velocity
	if collide:
		player_rect.bottom = rect.top
		player_rect.left += platform_vel

	# Adding platform_vel to x
	# coordinate of our rect
	rect.left += platform_vel

	# Adding gravity
	player_rect.top += gravity

	# Drawing the rect on the screen using the
	# draw.rect() method
	pygame.draw.rect(window, (255, 0, 0),rect)

	# Drawing player rect
	pygame.draw.rect(window, (0, 255, 0),player_rect)

	# Updating the display surface
	pygame.display.update()

	# Filling the window with white color
	window.fill((255,255,255))
