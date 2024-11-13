# Intro screen
def intro_loop():
	intro = True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				sys.exit()

		# Display background image
		gamedisplays.blit(intro_background,
						(0, 0))

		# Render and display "CAR GAME" text
		largetext = pygame.font.Font
					('freesansbold.ttf', 115)
		TextSurf, TextRect = text_objects
						("CAR GAME", largetext)
		TextRect.center = (400, 100)
		gamedisplays.blit(TextSurf, TextRect)

		# Render and display "START" button
		button("START", 150, 520, 100, 50, green,
								bright_green, "play")

		# Render and display "QUIT" button
		button("QUIT", 550, 520, 100, 50, red,
								bright_red, "quit")

		# Render and display "INSTRUCTION" button
		button("INSTRUCTION", 300, 520, 200,
					50, blue, bright_blue, "intro")

		pygame.display.update()
		clock.tick(50)
