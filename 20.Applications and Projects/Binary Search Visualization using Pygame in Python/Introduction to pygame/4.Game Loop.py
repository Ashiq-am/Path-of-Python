while running:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_BACKSPACE:
				running = False
		elif event.type == QUIT:
			running = False
