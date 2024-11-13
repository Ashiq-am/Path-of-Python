# gaming Loop
running = True
while running:

	# background color
	screen.fill(red)

	# to exit the loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
