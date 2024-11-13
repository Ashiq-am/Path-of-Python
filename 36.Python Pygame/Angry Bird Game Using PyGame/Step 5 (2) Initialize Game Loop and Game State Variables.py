# Enter the game loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		# Handle button clicks and player interactions
		if event.type == pygame.MOUSEBUTTONDOWN:
			# Check if the Quit button was clicked
			if quit_button.rect.collidepoint(event.pos):
				pygame.quit()
				sys.exit()

			# Check if the Refresh button was clicked
			elif refresh_button.rect.collidepoint(event.pos):
				# Reset player bird's position and velocity
				player_bird.rect.center = (100, SCREEN_HEIGHT // 2)
				player_bird.velocity = [0, 0]

				# Reset enemy birds and their positions
				enemy_birds.empty()
				for _ in range(5):
					x = random.randint(SCREEN_WIDTH // 2, SCREEN_WIDTH - 50)
					y = random.randint(50, SCREEN_HEIGHT - 50)
					enemy_bird = Bird(x, y, enemy_bird_image)
					enemy_birds.add(enemy_bird)

				# Reset game state
				level_cleared = False
				game_over = False
				try_again_counter = 0
				score = 0

			# Check if the player bird was clicked
			elif player_bird.rect.collidepoint(event.pos):
				player_bird.start_drag()

		elif event.type == pygame.MOUSEBUTTONUP:
			if player_bird.dragging:
				player_bird.end_drag()

				# Increment try_again_counter if no hits occurred
				if not hits:
					try_again_counter += 1
			else:
				break
