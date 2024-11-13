# Load bird and background images
player_bird_image = pygame.image.load(
	"angry_bird_pygame/Images/player_bird1.png")
enemy_bird_image = pygame.image.load(
	"angry_bird_pygame/Images/enemy_bird1.png")
background_image = pygame.image.load("angry_bird_pygame/Images/background.png")

# Scale the background image to fit the screen dimensions
background_image = pygame.transform.scale(
	background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
