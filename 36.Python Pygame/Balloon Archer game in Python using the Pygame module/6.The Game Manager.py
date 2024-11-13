# Game Manager
def main():
	score = 0
	lives = 5
	running = True

	archer = Archer(60, 60, 7)
	xFac, yFac = 0, 0 # Used to control the archer

	numBalloons = 10

	listOfBalloons = populateBalloons(30, 40, 5, numBalloons)
	listOfArrows = []

	while running:
		screen.fill(GREEN) # Background

		# Representing each life with an arrow tilted by 45 degrees
		for i in range(lives):
			screen.blit(pygame.transform.rotate(pygame.transform.scale(
				pygame.image.load(arrowPath), (20, 30)), 45), (i*30, 10))

		# Rendering the score
		scoreText = font.render(f"Score: {score}", True, WHITE)
		screen.blit(scoreText, (10, HEIGHT-50))

		if len(listOfBalloons) == 0:
			listOfBalloons = populateBalloons(30, 40, 5, numBalloons)

		# When all the lives are over
		if lives <= 0:
			running = gameOver()

			# Clearing the lists
			listOfBalloons.clear()
			listOfArrows.clear()

			# Resetting the variables
			lives = 5
			score = 0
			listOfBalloons = populateBalloons(30, 40, 5, numBalloons)

		# Display and update all the balloons
		for balloon in listOfBalloons:
			balloon.update()
			balloon.display()

		# Display and update all the arrows
		for arrow in listOfArrows:
			arrow.update()
			arrow.display()

		# Display and update the archer
		archer.display()
		archer.update(xFac, yFac)

		# Event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			# Key press event
			if event.type == pygame.KEYDOWN:
				# Replay button
				if event.key == pygame.K_r:
					listOfBalloons = populateBalloons(30, 40, 5, numBalloons)
					score = 0
				# Right arrow key => move rightwards => xFac = 1
				if event.key == pygame.K_RIGHT:
					xFac = 1
				# Left arrow key => move leftwards => xFac = -1
				if event.key == pygame.K_LEFT:
					xFac = -1
				# Down arrow key => move downwards => yFac = 1
				if event.key == pygame.K_DOWN:
					yFac = 1
				# Up arrow key => move upwards => yFac = -1
				if event.key == pygame.K_UP:
					yFac = -1
				# Fire button
				if event.key == pygame.K_SPACE:
					listOfArrows.append(Arrow(
						archer.archerRect.x,
						archer.archerRect.y+archer.archerRect.h/2-15, 60, 30, 10))

			# Key release event
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
					xFac = 0
				if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
					yFac = 0

		# Check for any collision between the arrows and the balloons
		for arrow in listOfArrows:
			for balloon in listOfBalloons:
				if pygame.Rect.colliderect(arrow.arrowRect, balloon.balloonRect):
					# Changes the arrow's 'hit' from 0 to 1
					arrow.updateHit()
					# Remove the balloon form the list
					listOfBalloons.pop(listOfBalloons.index(balloon))
					# Increase the score
					score += 1

		# Delete the arrows that crossed end of the screen
		for arrow in listOfArrows:
			if arrow.arrowRect.x > WIDTH:
				if not arrow.getHit():
					# If the arrow's state is 0, then a life is deducted
					lives -= 1
				listOfArrows.pop(listOfArrows.index(arrow))

		pygame.display.update()
		clock.tick(FPS)
