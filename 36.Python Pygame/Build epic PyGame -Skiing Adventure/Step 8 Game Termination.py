def main():
	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load(cfg.BGMPATH)
	pygame.mixer.music.set_volume(0.4)
	pygame.mixer.music.play(-1)

	screen = pygame.display.set_mode(cfg.SCREENSIZE)
	pygame.display.set_caption('Skier Game')

	ShowStartInterface(screen, cfg.SCREENSIZE)

	while True:
		skier = SkierClass()
		# Decrease number of trees and stones
		obstacles0 = createObstacles(20, 29, num=15)
		obstacles1 = createObstacles(10, 19, num=15)
		obstaclesflag = 0
		obstacles = AddObstacles(obstacles0, obstacles1)
		clock = pygame.time.Clock()
		distance = 0
		# Variable to track whether the game should restart or quit
		restart = False

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT or event.key == pygame.K_a:
						skier.turn(-1)
					elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
						skier.turn(1)
					# Press 'q' to quit the game
					elif event.key == pygame.K_q:
						pygame.quit()
						sys.exit()
					# Press 'r' to restart the game
					elif event.key == pygame.K_r:
						restart = True
			# Exit the inner loop to restart the game
			if restart:
				break

			skier.move()
			distance += skier.speed[1]
			if distance >= 640 and obstaclesflag == 0:
				obstaclesflag = 1
				# Decrease number of trees and stones
				obstacles0 = createObstacles(20, 29, num=15)
				obstacles = AddObstacles(obstacles0, obstacles1)

			if distance >= 1280 and obstaclesflag == 1:
				obstaclesflag = 0
				distance -= 1280
				for obstacle in obstacles0:
					obstacle.location[1] = obstacle.location[1] - 1280
				# Decrease number of trees and stones
				obstacles1 = createObstacles(10, 19, num=15)
				obstacles = AddObstacles(obstacles0, obstacles1)

			for obstacle in obstacles:
				obstacle.move(distance)

			hitted_obstacles = pygame.sprite.spritecollide(skier, obstacles, False)
			if hitted_obstacles:
				if hitted_obstacles[0].attribute == "tree" and not hitted_obstacles[0].passed:
					# Decrease score by 5 when hitting a tree
					skier.score -= 5
					skier.setFall()
					# Decrease skier's speed
					skier.speed[1] = 2
					updateFrame(screen, obstacles, skier)
					pygame.time.delay(1000)
					skier.setForward()
					# Reset skier's speed
					skier.speed[1] = 6
					hitted_obstacles[0].passed = True
				elif hitted_obstacles[0].attribute == "stone" and not hitted_obstacles[0].passed:
					# Decrease score by 10 when hitting a stone
					skier.score -= 10
					skier.setFall()
					# Decrease skier's speed
					skier.speed[1] = 2
					updateFrame(screen, obstacles, skier)
					pygame.time.delay(1000)
					skier.setForward()
					# Reset skier's speed
					skier.speed[1] = 6
					hitted_obstacles[0].passed = True
				elif hitted_obstacles[0].attribute == "flag" and not hitted_obstacles[0].passed:
					# Increase score by 10 when collecting a flag
					skier.score += 10
					skier.flag_count += 1
					# Increase speed after collecting 10 flags
					if skier.flag_count >= 10:
						skier.speed[1] = 8
					obstacles.remove(hitted_obstacles[0])

			updateFrame(screen, obstacles, skier)
			if skier.score < 0:
				# Check if score is negative
				screen.fill((255, 255, 255))
				font = pygame.font.Font(cfg.FONTPATH, 40)
				game_over_text = font.render("Game Over", True, (255, 0, 0))
				prompt_text = font.render("Press 'r' to restart or 'q' to quit.", True, (0, 0, 255))
				game_over_rect = game_over_text.get_rect(center=(cfg.SCREENSIZE[0] // 2, cfg.SCREENSIZE[1] // 2))
				prompt_rect = prompt_text.get_rect(center=(cfg.SCREENSIZE[0] // 2, cfg.SCREENSIZE[1] // 2 + 50))
				screen.blit(game_over_text, game_over_rect)
				screen.blit(prompt_text, prompt_rect)
				pygame.display.update()

				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
							sys.exit()
						if event.type == pygame.KEYDOWN:
						# Press 'r' to restart the game
							if event.key == pygame.K_r:
								restart = True
							# Press 'q' to quit the game
							elif event.key == pygame.K_q:
								pygame.quit()
								sys.exit()
					# Exit the inner loop to restart the game
					if restart:
						break

			clock.tick(cfg.FPS)
		# Exit the outer loop if the game should quit
		if not restart:
			break

if __name__ == '__main__':
	main()
