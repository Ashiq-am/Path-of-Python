def countdown():
	# Initialize a boolean variable to indicate if countdown is i
		# n progress
	countdown = True
	# Continue looping until countdown is complete
	while countdown:
		# Check for events in the pygame event queue
		for event in pygame.event.get():
			# If user closes the game window
			if event.type == pygame.QUIT:
				pygame.quit() # Quit pygame
				quit() # Quit the game
				sys.exit() # Exit the program
		# Fill the game display with a gray color
		gamedisplays.fill(gray)
		# Call a function to display the countdown background
		countdown_background()

		# Display "3" in large font at the center of the screen
		largetext = pygame.font.Font('freesansbold.ttf', 115)
		TextSurf, TextRect = text_objects("3", largetext)
		TextRect.center = ((display_width/2), (display_height/2))
		gamedisplays.blit(TextSurf, TextRect)
		pygame.display.update()
		clock.tick(1) # Delay for 1 second

		gamedisplays.fill(gray)
		countdown_background()

		# Display "2" in large font at the center of the screen
		largetext = pygame.font.Font('freesansbold.ttf', 115)
		TextSurf, TextRect = text_objects("2", largetext)
		TextRect.center = ((display_width/2), (display_height/2))
		gamedisplays.blit(TextSurf, TextRect)
		pygame.display.update()
		clock.tick(1) # Delay for 1 second

		gamedisplays.fill(gray)
		countdown_background()

		# Display "1" in large font at the center of the screen
		largetext = pygame.font.Font('freesansbold.ttf', 115)
		TextSurf, TextRect = text_objects("1", largetext)
		TextRect.center = ((display_width/2), (display_height/2))
		gamedisplays.blit(TextSurf, TextRect)
		pygame.display.update()
		clock.tick(1) # Delay for 1 second

		gamedisplays.fill(gray)
		countdown_background()

		# Display "GO!!!" in large font at the center of the screen
		largetext = pygame.font.Font('freesansbold.ttf', 115)
		TextSurf, TextRect = text_objects("GO!!!", largetext)
		TextRect.center = ((display_width/2), (display_height/2))
		gamedisplays.blit(TextSurf, TextRect)
		pygame.display.update()
		clock.tick(1) # Delay for 1 second
		# Call the game loop function after the countdown is complete
		game_loop()
