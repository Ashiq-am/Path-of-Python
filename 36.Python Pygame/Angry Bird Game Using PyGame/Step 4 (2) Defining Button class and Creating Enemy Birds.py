# Create the player bird
player_bird = Bird(100, SCREEN_HEIGHT // 2, player_bird_image)

# Create enemy birds
enemy_birds = pygame.sprite.Group()
for _ in range(5):
	x = random.randint(SCREEN_WIDTH // 2, SCREEN_WIDTH - 50)
	y = random.randint(50, SCREEN_HEIGHT - 50)
	enemy_bird = Bird(x, y, enemy_bird_image)
	enemy_birds.add(enemy_bird)
