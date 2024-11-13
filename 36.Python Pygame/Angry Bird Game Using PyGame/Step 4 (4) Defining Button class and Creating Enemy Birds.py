# Create quit and refresh buttons
quit_button_image = pygame.image.load(
	"angry_bird_pygame/Images/quit_button.png")
refresh_button_image = pygame.image.load(
	"angry_bird_pygame/Images/refresh_button.png")

quit_button = Button(button_left, button_top, quit_button_image, "quit")
refresh_button = Button(button_left + quit_button_image.get_width() +
						button_spacing, button_top,
						refresh_button_image, "refresh")
