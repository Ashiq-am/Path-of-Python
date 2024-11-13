# If its game_page then draw circles, tiles, balls, score board
	# and particle spin offs
if game_page:
		pygame.draw.circle(win, BLACK, CENTER, 80, 20)
		ball_group.update(color)
		coin_group.update(color)
		tile_group.update()
		score_msg.update(score)
		particle_group.update()
		# If player is alive then the balls obstacle
		# and coins movement will initiate
		if player_alive:
			for ball in ball_group:
				if pygame.sprite.spritecollide(ball,
									coin_group, True):
					score_fx.play()
					score += 1
					# Score updation
					if highscore <= score:
						highscore = score

					x, y = ball.rect.center
					for i in range(10):
						particle = Particle(x, y, color, win)
						particle_group.add(particle)
				# If ball gets collided with tile
				# then player_alive becomes false
				# and trigger dead sound
				if pygame.sprite.spritecollide(ball,
										tile_group, True):
					x, y = ball.rect.center
					for i in range(30):
						particle = Particle(x, y, color, win)
						particle_group.add(particle)

					player_alive = False
					dead_fx.play()
			# time frame of game
			current_time = pygame.time.get_ticks()
			delta = current_time - start_time
			# Create obstacle coins and once created
			# turn off the boolean
			if coin_delta < delta < coin_delta + 100 and new_coin:
				y = random.randint(CENTER[1]-RADIUS,
								CENTER[1]+RADIUS)
				coin = Coins(y, win)
				coin_group.add(coin)
				new_coin = False
			# if current_time - start_time is greater
			# or equals to tile_delta
			# then create new coin in the obstacle form
			if current_time - start_time >= tile_delta:
				y = random.choice([CENTER[1]-80,
								CENTER[1], CENTER[1]+80])
				type_ = random.randint(1, 3)
				t = Tiles(y, type_, win)
				tile_group.add(t)

				start_time = current_time
				new_coin = True
		# when player is dead
		if not player_alive and len(particle_group) == 0:
			score_page = True
			game_page = False

			score_page_fx.play()

			ball_group.empty()
			tile_group.empty()
			coin_group.empty()
	# Game screen
	pygame.draw.rect(win, BLUE, (0, 0, WIDTH, HEIGHT),
					5, border_radius=10)
	# Screen FPS
	clock.tick(FPS)
	# updates display
	pygame.display.update()
