def ShowStartInterface(screen, screensize):
	#white color
	screen.fill((255, 255, 255))
	#title font
	tfont = pygame.font.Font(cfg.FONTPATH, screensize[0] // 5)
	#content font
	cfont = pygame.font.Font(cfg.FONTPATH, screensize[0] // 20)
	#red color
	title = tfont.render(u'Skier Game', True, (255, 0, 0))
	# Content text in blue color
	content = cfont.render(u'Press any key to START.', True, (0, 0, 255))

	trect = title.get_rect()
	# Set the position of the title text at the top center
	trect.midtop = (screensize[0] / 2, screensize[1] / 5)
	crect = content.get_rect()
	crect.midtop = (screensize[0] / 2, screensize[1] / 2)
	# Blit (draw) the title text onto the screen at the specified position
	screen.blit(title, trect)
	screen.blit(content, crect)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
			# Exit the function and start the game when any key is pressed
				return

		pygame.display.update()
