# Function to display the introduction screen
def introduction():
	introduction = True
	while introduction:
		# Get events from the event queue
		for event in pygame.event.get():
			# If the 'QUIT' event is triggered
			# (e.g., window closed)
			if event.type == pygame.QUIT:
				pygame.quit() # Quit pygame
				quit() # Quit the game
				sys.exit() # Exit the system
		# Draw the instruction background
		gamedisplays.blit(instruction_background, (0, 0))
		# Set font for large text
		largetext = pygame.font.Font('freesansbold.ttf', 80)
		# Set font for small text
		smalltext = pygame.font.Font('freesansbold.ttf', 20)
		# Set font for medium text
		mediumtext = pygame.font.Font('freesansbold.ttf', 40)

		# Render and draw the instruction text
		textSurf, textRect = text_objects("This is an car game" +
			"in which you need dodge the coming cars", smalltext)
		textRect.center = ((350), (200))
		TextSurf, TextRect = text_objects("INSTRUCTION", largetext)
		TextRect.center = ((400), (100))
		gamedisplays.blit(TextSurf, TextRect)
		gamedisplays.blit(textSurf, textRect)

		# Render and draw the control instructions
		stextSurf, stextRect = text_objects(
			"ARROW LEFT : LEFT TURN", smalltext)
		stextRect.center = ((150), (400))
		hTextSurf, hTextRect = text_objects(
			"ARROW RIGHT : RIGHT TURN", smalltext)
		hTextRect.center = ((150), (450))
		atextSurf, atextRect = text_objects
					("A : ACCELERATOR", smalltext)
		atextRect.center = ((150), (500))
		rtextSurf, rtextRect = text_objects
						("B : BRAKE ", smalltext)
		rtextRect.center = ((150), (550))
		ptextSurf, ptextRect = text_objects
						("P : PAUSE ", smalltext)
		ptextRect.center = ((150), (350))
		sTextSurf, sTextRect = text_objects
							("CONTROLS", mediumtext)
		sTextRect.center = ((350), (300))
		gamedisplays.blit(sTextSurf, sTextRect)
		gamedisplays.blit(stextSurf, stextRect)
		gamedisplays.blit(hTextSurf, hTextRect)
		gamedisplays.blit(atextSurf, atextRect)
		gamedisplays.blit(rtextSurf, rtextRect)
		gamedisplays.blit(ptextSurf, ptextRect)

		# Render and draw the 'BACK' button
		button("BACK", 600, 450, 100, 50, blue,
							bright_blue, "menu")

		pygame.display.update() # Update the display
		clock.tick(30) # Limit frame rate to 30 FPS
