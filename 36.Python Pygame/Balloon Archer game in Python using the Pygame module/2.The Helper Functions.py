# Spawn the balloons
def populateBalloons(bWidth, bHeight, bSpeed, bCount):
	listOfBalloons = []

	# For the given count, spawn balloons at random
	# positions in the right half of the screen with
	# the given dimensions and speed
	for _ in range(bCount):
		listOfBalloons.append(Balloon(random.randint(
			WIDTH//2, WIDTH-bWidth), random.randint(0, HEIGHT),
									bWidth, bHeight, bSpeed))

	return listOfBalloons


# Game Over Screen. Waits for the user to replay or quit
def gameOver():
	gameOver = True

	while gameOver:
		gameOverText = font.render("GAME OVER", True, WHITE)
		retryText = font.render("R - Replay Q - Quit", True, WHITE)

		# render the text on the screen using the pygame blit function
		screen.blit(gameOverText, (WIDTH//2-200, HEIGHT//2-100))
		screen.blit(retryText, (WIDTH//2-200, HEIGHT//2-80))

		# Event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False
			if event.type == pygame.KEYDOWN:
				# replay
				if event.key == pygame.K_r:
					return True
				# quit
				if event.key == pygame.K_q:
					return False

		pygame.display.update()
