def paused():
	global pause

	# Loop for handling events during pause state
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				sys.exit()
		gamedisplays.blit(instruction_background,
						(0, 0))
		largetext = pygame.font.Font('freesansbold.ttf',
							115)
		TextSurf, TextRect = text_objects("PAUSED",
							largetext)
		TextRect.center = (
		(display_width/2),
		(display_height/2))
		gamedisplays.blit(TextSurf, TextRect)
		# Create buttons for continue, restart, and main menu
		button("CONTINUE", 150,
			450, 150, 50,
			green, bright_green, "unpause")
		button("RESTART", 350,
			450, 150, 50,
			blue, bright_blue, "play")
		button("MAIN MENU", 550,
			450, 200, 50,
			red, bright_red, "menu")
		pygame.display.update()
		clock.tick(30)


def unpaused():
	global pause
	pause = False
