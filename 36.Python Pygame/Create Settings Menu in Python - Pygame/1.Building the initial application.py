# Program to create a basic window using the pygame_menu module

import pygame
import pygame_menu as pm

pygame.init()

WIDTH, HEIGHT = 700, 600

# Screen and caption
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Window using Pygame_menu")


# Main Function
def mainFun():
	# Creating a menu
	menu = pm.Menu(title="Main Menu",
				width=WIDTH,
				height=HEIGHT,
				theme=pm.themes.THEME_GREEN)

	# Adding a label to the menu
	menu.add.label(title="This is a label on the Main Menu")

	# Displaying the menu on the screen using the "mainloop" method of pygame_menu.Menu
	menu.mainloop(screen)


if __name__ == "__main__":
	mainFun() # Calling the main function


# This code is contributed by Teja
