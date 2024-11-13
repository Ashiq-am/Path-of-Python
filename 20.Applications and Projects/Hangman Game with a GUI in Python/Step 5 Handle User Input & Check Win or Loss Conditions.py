while run:
	clock.tick(FPS)
	draw()

	for event in pygame.event.get(): # Triggering the event
		if event.type == pygame.QUIT:
			run = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			x_mouse, y_mouse = pygame.mouse.get_pos()

			for letter in letters:
				x, y, ltr, visible = letter

				if visible:
				# To handle collision and to click the button exactly in the circle
					dist = math.sqrt((x - x_mouse) ** 2 + (y - y_mouse) ** 2)

					if dist <= radius:
						letter[3] = False # To invisible the clicked button
						guessed.append(ltr)
						if ltr not in words:
							hangman += 1

	# Deciding if you won the game or not
	won = True
	for letter in words:
		if letter not in guessed:
			won = False
			break

	if won:
		draw()
		pygame.time.delay(1000)
		win.fill((0, 0, 0))
		text = WORD.render("YOU WON", 1, (129, 255, 0))
		win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
		pygame.display.update()
		pygame.time.delay(4000)
		print("WON")
		break

	if hangman == 6:
		draw()
		pygame.time.delay(1000)
		win.fill((0, 0, 0))
		text = WORD.render("YOU LOST", 1, (255, 0, 5))
		answer = WORD.render("The answer is " + words, 1, (129, 255, 0))
		win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
		win.blit(answer, ((WIDTH / 2 - answer.get_width() / 2),
						(HEIGHT / 2 - text.get_height() / 2) + 70))

		pygame.display.update()
		pygame.time.delay(4000)
		print("LOST")
		break

pygame.quit()
