# main loop
running = True
while running:
# fill with black color
	screen.fill((0, 0, 0))
	# start drawing the gui board of sliding puzzle
	pygame.draw.rect(screen, (165, 42, 42),
					pygame.Rect(95, 45, 620, 620))
	game_over_print = game_over_font.render(
		game_over_banner, True, (255, 255, 0))
	# blit() will take that rectangular
	# Surface and put it on top of the screen.
	screen.blit(game_over_print, (950, 100))

	# render the move_count with the use of str
	if move_count == 0:
		move_count_render = move_count_font.render(
			move_count_banner, True, (0, 255, 0))
	else:
		move_count_render = move_count_font.render(
			move_count_banner + str(move_count), True, (0, 255, 0))
	screen.blit(move_count_render, (1050, 200))

	# Get events from the queue.
	for event in pygame.event.get():
		# if its quite operation then exit the while loop
		if event.type == pygame.QUIT:
			running = False
		# if mouse click are detected
		# then find (x,y) and then pass
		# them to mouse_hover method
		if event.type == pygame.MOUSEMOTION:
			x_m_motion, y_m_motion = pygame.mouse.get_pos()
			for i in range(tile_count):
				tiles[i].mouse_hover(x_m_motion, y_m_motion)
			# if the tile is selected &
			# mouse is pressed then pass
			# the coords to move_tyle method
			for i in range(tile_count):
				if tiles[i].selected and mouse_press:
					tiles[i].move_tyle(x_m_motion, y_m_motion)
		# Moving tile downwards
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_press = True
			x_m_click, y_m_click = pygame.mouse.get_pos()
			for i in range(tile_count):
				tiles[i].mouse_click(x_m_click, y_m_click)
		# Moving tile upwards
		if event.type == pygame.MOUSEBUTTONUP:
			mouse_press = False
			x_m_click_rel, y_m_click_rel = pygame.mouse.get_pos()
			x_m_click, y_m_click = 0, 0
			cell_found = False
			for i in range(0, rows):
				for j in range(0, cols):
					tile_start_pos_x = tile_print_position[(i, j)][0]
					tile_start_pos_y = tile_print_position[(i, j)][1]

					if (x_m_click_rel > tile_start_pos_x
						and x_m_click_rel < tile_start_pos_x + tile_width) and (y_m_click_rel > tile_start_pos_y and y_m_click_rel < tile_start_pos_y + tile_depth):
						if matrix[i][j] == "":
							for k in range(tile_count):
								if game_over == False:
									if tiles[k].selected:
										if tiles[k].movable:
											cell_found = True
											dummy = matrix[tiles[k].position_x][tiles[k].position_y]
											matrix[tiles[k].position_x][tiles[k].position_y] = matrix[i][j]
											matrix[i][j] = dummy
											tiles[k].position_x = i
											tiles[k].position_y = j
											tiles[k].start_pos_x = tile_print_position[(
												i, j)][0]
											tiles[k].start_pos_y = tile_print_position[(
												i, j)][1]
											move_count += 1
											isGameOver()
											check_mobility()

					if cell_found == False:
						for k in range(tile_count):
							if tiles[k].selected:
								mat_pos_x = tiles[k].position_x
								mat_pos_y = tiles[k].position_y
								tiles[k].start_pos_x = tile_print_position[(
									mat_pos_x, mat_pos_y)][0]
								tiles[k].start_pos_y = tile_print_position[(
									mat_pos_x, mat_pos_y)][1]
								break
