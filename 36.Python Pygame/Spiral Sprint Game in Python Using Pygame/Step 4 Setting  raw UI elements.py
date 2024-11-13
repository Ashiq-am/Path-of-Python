# Set the defaut FPS of the game as 90
clock = pygame.time.Clock()
FPS = 90

# COLORS
RED = (255, 0, 0)
GREEN = (0, 177, 64)
BLUE = (30, 144, 255)
ORANGE = (252, 76, 2)
YELLOW = (254, 221, 0)
PURPLE = (155, 38, 182)
AQUA = (0, 103, 127)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (25, 25, 25)

color_list = [PURPLE, GREEN, BLUE, ORANGE, YELLOW, RED]
color_index = 0
color = color_list[color_index]

# SOUNDS
flip_fx = pygame.mixer.Sound('Sounds/flip.mp3')
score_fx = pygame.mixer.Sound('Sounds/point.mp3')
dead_fx = pygame.mixer.Sound('Sounds/dead.mp3')
score_page_fx = pygame.mixer.Sound('Sounds/score_page.mp3')

# Now set the sound at transition point of the game
pygame.mixer.music.load('Sounds/bgm.mp3')
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.5)

# FONTS
title_font = "Fonts/Aladin-Regular.ttf"
score_font = "Fonts/DroneflyRegular-K78LA.ttf"
game_over_font = "Fonts/ghostclan.ttf"
final_score_font = "Fonts/DalelandsUncialBold-82zA.ttf"
new_high_font = "Fonts/BubblegumSans-Regular.ttf"

# Using different font for differrent texts to look more curated for that screen
connected = Message(WIDTH//2, 120, 55, "Spiral Sprint", title_font, WHITE, win)
score_msg = Message(WIDTH//2, 100, 60, "0", score_font, (150, 150, 150), win)
game_msg = Message(80, 150, 40, "GAME", game_over_font, BLACK, win)
over_msg = Message(210, 150, 40, "OVER!", game_over_font, WHITE, win)
final_score = Message(WIDTH//2, HEIGHT//2, 90, "0", final_score_font, RED, win)
new_high_msg = Message(WIDTH//2, HEIGHT//2+60, 20,
					"New High", None, GREEN, win)

# Declaring Button images
home_img = pygame.image.load('Assets/homeBtn.png')
replay_img = pygame.image.load('Assets/replay.png')
sound_off_img = pygame.image.load("Assets/soundOffBtn.png")
sound_on_img = pygame.image.load("Assets/soundOnBtn.png")
easy_img = pygame.image.load("Assets/easy.jpg")
hard_img = pygame.image.load("Assets/hard.jpg")

# Buttons
easy_btn = Button(easy_img, (70, 24), WIDTH//4-10, HEIGHT-100)
hard_btn = Button(hard_img, (70, 24), WIDTH//2 + 10, HEIGHT-100)
home_btn = Button(home_img, (24, 24), WIDTH // 4 - 18, HEIGHT//2 + 120)
replay_btn = Button(replay_img, (36, 36), WIDTH // 2 - 18, HEIGHT//2 + 115)
sound_btn = Button(sound_on_img, (24, 24), WIDTH -
				WIDTH // 4 - 18, HEIGHT//2 + 120)
