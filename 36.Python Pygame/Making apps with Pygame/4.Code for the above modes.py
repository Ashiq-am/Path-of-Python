import pygame as py
from pygame.locals import *

# Create a displace surface object
py.init()

# Un-comment one of the following
# three line of code for varied mode of pygame
# display_surface = py.display.set_mode((500, 250), NOFRAME)
# display_surface = py.display.set_mode((500, 250), FULLSCREEN)
display_surface = py.display.set_mode((500, 250), RESIZABLE)

working = True
while working: # run until it become false
	for event in py.event.get():
		if event.type == py.QUIT:
			working = False
	py.display.update()

py.quit() # quit the window
