for event in pygame. event.get():
	if event.type == pygame.QUIT:
		raise SystemExit
	elif event.type == pygame.MOUSEMOTION:
		if event.rel[0] > 0:
			print("Mouse moving to the right")
		elif event.rel[1] > 0:
			print("Mouse moving down")
	elif event.type == pygame.MOUSEBUTTONDOWN:
		if event.button == 3:
			print("Right mouse button pressed")
	elif event.type == pygame.MOUSEBUTTONUP:
		print("Mouse button has been released")
