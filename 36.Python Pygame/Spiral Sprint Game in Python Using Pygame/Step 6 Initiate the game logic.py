running = True
# While the game is running
while running:
	# Fill the game window with GRAY color
	win.fill(GRAY)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		# If the event is quit then off the
		# bool running and quit the window
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE or \
					event.key == pygame.K_q:
				running = False

		# If the event detected is a type of click
		# then on the bool clicked and perform that task
		if event.type == pygame.MOUSEBUTTONDOWN and game_page:
			if not clicked:
				clicked = True
				# Just reverse their rotation direction
				# when clicked[Multiply by -1]
				for ball in ball_group:
					ball.dtheta *= -1
					flip_fx.play()
				# change the color of ball ater every
				# 5 click to make it more alive
				num_clicks += 1
				if num_clicks % 5 == 0:
					color_index += 1
					if color_index > len(color_list) - 1:
						color_index = 0

					color = color_list[color_index]

		if event.type == pygame.MOUSEBUTTONDOWN and game_page:
			clicked = False
