import pygame
import pygame_menu as pm

pygame.init()

# Screen
WIDTH, HEIGHT = 700, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Standard RGB colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 100, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Main Function
def mainFun():
	mainMenu = pm.Menu(title="Main Menu",
					width=WIDTH,
					height=HEIGHT,
					theme=pm.themes.THEME_GREEN)

	# Settings button. If clicked, it takes to the settings menu
	mainMenu.add.button(title="Settings", font_color=WHITE,
						background_color=GREEN)

	# Dummy label to add some spacing between the settings button and exit button
	mainMenu.add.label(title="")

	# Exit Button. If clicked, it closes the window
	mainMenu.add.button(title="Exit", action=pm.events.EXIT,
						font_color=WHITE, background_color=RED)

	mainMenu.mainloop(screen)


if __name__ == "__main__":
	mainFun()
