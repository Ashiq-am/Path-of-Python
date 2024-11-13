# Game Manager
def main():
	running = True
	lives = 3
	score = 0

	scoreText = font.render("score", True, WHITE)
	scoreTextRect = scoreText.get_rect()
	scoreTextRect.center = (20, HEIGHT-10)

	livesText = font.render("Lives", True, WHITE)
	livesTextRect = livesText.get_rect()
	livesTextRect.center = (120, HEIGHT-10)

	striker = Striker(0, HEIGHT-50, 100, 20, 10, WHITE)
	strikerXFac = 0

	ball = Ball(0, HEIGHT-150, 7, 5, WHITE)

	blockWidth, blockHeight = 40, 15
	horizontalGap, verticalGap = 20, 20

	listOfBlocks = populateBlocks(
		blockWidth, blockHeight, horizontalGap, verticalGap)

	# Game loop
	while running:
		screen.fill(BLACK)
		screen.blit(scoreText, scoreTextRect)
		screen.blit(livesText, livesTextRect)

		scoreText = font.render("Score : " + str(score), True, WHITE)
		livesText = font.render("Lives : " + str(lives), True, WHITE)

		# If all the blocks are destroyed, then we repopulate them
		if not listOfBlocks:
			listOfBlocks = populateBlocks(
				blockWidth, blockHeight, horizontalGap, verticalGap)

		# All the lives are over. So, the gameOver() function is called
		if lives <= 0:
			running = gameOver()

			while listOfBlocks:
				listOfBlocks.pop(0)

			lives = 3
			score = 0
			listOfBlocks = populateBlocks(
				blockWidth, blockHeight, horizontalGap, verticalGap)

		# Event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					strikerXFac = -1
				if event.key == pygame.K_RIGHT:
					strikerXFac = 1

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					strikerXFac = 0

		# Collision check
		if(collisionChecker(striker.getRect(), ball.getRect())):
			ball.hit()
		for block in listOfBlocks:
			if(collisionChecker(block.getRect(), ball.getRect())):
				ball.hit()
				block.hit()

				if block.getHealth() <= 0:
					listOfBlocks.pop(listOfBlocks.index(block))
					score += 5

		# Update
		striker.update(strikerXFac)
		lifeLost = ball.update()

		if lifeLost:
			lives -= 1
			ball.reset()
			print(lives)

		# Display
		striker.display()
		ball.display()

		for block in listOfBlocks:
			block.display()

		pygame.display.update()
		clock.tick(FPS)


# This code is contributed by teja00219
