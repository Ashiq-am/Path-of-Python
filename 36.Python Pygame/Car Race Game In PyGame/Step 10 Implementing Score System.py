def score_system(passed, score):
	# Create a font object with size 25
	font = pygame.font.SysFont(None, 25)
	# Render the "Passed" text with passed parameter
	# and color black
	text = font.render("Passed"+str(passed), True, black)
	# Render the "Score" text with score parameter and color red
	score = font.render("Score"+str(score), True, red)
	# Draw the "Passed" text on the game display at (0, 50)
	# coordinates
	gamedisplays.blit(text, (0, 50))
	# Draw the "Score" text on the game display at (0, 30)
	# coordinates
	gamedisplays.blit(score, (0, 30))


def text_objects(text, font):
	# Render the given text with the given font and color black
	textsurface = font.render(text, True, black)
	return textsurface, textsurface.get_rect()


def message_display(text):
	# Create a font object with size 80
	largetext = pygame.font.Font("freesansbold.ttf", 80)
	# Render the given text with the created font
	textsurf, textrect = text_objects(text, largetext)
	textrect.center = ((display_width/2), (display_height/2))
	# Draw the rendered text on the game display at the center of the
	# screen
	gamedisplays.blit(textsurf, textrect)
	pygame.display.update()
	time.sleep(3)
	game_loop()
