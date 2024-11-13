# Groups
RADIUS = 70 # Defining circle radius
ball_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
tile_group = pygame.sprite.Group()
particle_group = pygame.sprite.Group()

# One ball above the diameter
# i.e first and second quadrant
ball = Balls((CENTER[0], CENTER[1]+RADIUS),
			RADIUS, 90, win)
ball_group.add(ball)
# Second ball below the diameter
# i.e third and fourth quadrant
ball = Balls((CENTER[0], CENTER[1]-RADIUS),
			RADIUS, 270, win)
ball_group.add(ball)

# TIME
# Time interval at which the tiles should arive
# so the user has a scope of dodging
start_time = pygame.time.get_ticks()
current_time = 0
coin_delta = 850
tile_delta = 2000

# BOOL VARIABLES
clicked = False
new_coin = True
num_clicks = 0
score = 0

player_alive = True
score = 0
highscore = 0
sound_on = True
easy_level = True

home_page = True
game_page = False
score_page = False
