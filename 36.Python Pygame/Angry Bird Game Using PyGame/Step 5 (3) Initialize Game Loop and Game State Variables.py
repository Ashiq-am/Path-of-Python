# Update enemy bird positions and handle collisions
hits = pygame.sprite.spritecollide(player_bird, enemy_birds, True)

if hits:
		for hit_enemy in hits:
			hit_enemy.hit_enemy()

	# Reset enemy bird positions
	for enemy_bird in enemy_birds:
		if enemy_bird.rect.right < 0:
			enemy_bird.rect.left = SCREEN_WIDTH
			enemy_bird.rect.top = random.randint(50, SCREEN_HEIGHT - 50)

	# Reset player bird's position if it goes off-screen
	if player_bird.rect.left > SCREEN_WIDTH or player_bird.rect.right < 0 or \
			player_bird.rect.top > SCREEN_HEIGHT or player_bird.rect.bottom < 0:
		player_bird.rect.center = (100, SCREEN_HEIGHT // 2)
		player_bird.velocity = [0, 0]
