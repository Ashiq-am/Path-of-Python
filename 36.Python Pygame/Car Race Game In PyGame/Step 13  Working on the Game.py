#!/usr/bin/python
# -*- coding: utf-8 -*-

def game_loop():
	global pause
	x = display_width * 0.45
	y = display_height * 0.8
	x_change = 0
	obstacle_speed = 9
	obs = 0
	y_change = 0
	obs_startx = random.randrange(200, display_width - 200)
	obs_starty = -750
	obs_width = 56
	obs_height = 125
	passed = 0
	level = 0
	score = 0
	y2 = 7
	fps = 120

	# flag to indicate that the player has been crashed

	bumped = False

	while not bumped:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				if event.key == pygame.K_RIGHT:
					x_change = 5
				if event.key == pygame.K_a:
					obstacle_speed += 2
				if event.key == pygame.K_b:
					obstacle_speed -= 2
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					x_change = 0
				if event.key == pygame.K_RIGHT:
					x_change = 0

		# Update player's car position

	x += x_change

	# Set pause flag to True

	pause = True

	# Fill the game display with gray color

	gamedisplays.fill(gray)

	# Update background position

	rel_y = y2 % backgroundpic.get_rect().width
	gamedisplays.blit(backgroundpic, (0, rel_y
									- backgroundpic.get_rect().width))
	gamedisplays.blit(backgroundpic, (700, rel_y
									- backgroundpic.get_rect().width))

	# Draw background strips

	if rel_y < 800:

		# Draw background strips

		gamedisplays.blit(backgroundpic, (0, rel_y))
		gamedisplays.blit(backgroundpic, (700, rel_y))
		gamedisplays.blit(yellow_strip, (400, rel_y))
		gamedisplays.blit(yellow_strip, (400, rel_y + 100))

	# Update obstacle positions and display them

	y2 += obstacle_speed
	obs_starty -= obstacle_speed / 4
	obstacle(obs_startx, obs_starty, obs)
	obs_starty += obstacle_speed

	# Update player's car position and display it

	car(x, y)

	# Update score system and display score

	score_system(passed, score)

	# Check for collision with screen edges and call crash()
	# function if collision occurs

	if x > 690 - car_width or x < 110:
		crash()
	if x > display_width - (car_width + 110):
		crash()
	if x < 110:
		crash()

	# Update obstacle positions and display them

	if obs_starty > display_height:
		obs_starty = 0 - obs_height
		obs_startx = random.randrange(170, display_width - 170)
		obs = random.randrange(0, 7)
		passed = passed + 1
		score = passed * 10

		# Check for level up and update obstacle speed, display
		# level text, and pause for 3 seconds

		if int(passed) % 10 == 0:
			level = level + 1
			obstacle_speed += 2
			largetext = pygame.font.Font('freesansbold.ttf', 80)
			(textsurf, textrect) = text_objects('LEVEL' + str(level),
												largetext)
			textrect.center = (display_width / 2, display_height / 2)
			gamedisplays.blit(textsurf, textrect)
			pygame.display.update()
			time.sleep(3)

	# Check for collision with obstacles and call crash()
	# function if collision occurs

	if y < obs_starty + obs_height:
		if x > obs_startx and x < obs_startx + obs_width or x \
			+ car_width > obs_startx and x + car_width < obs_startx \
				+ obs_width:
			crash()

	# Draw pause button

	button(
		'Pause',
		650,
		0,
		150,
		50,
		blue,
		bright_blue,
		'pause',
	)

	# Update game display and set frames per second to 60

	pygame.display.update()
	clock.tick(60)
