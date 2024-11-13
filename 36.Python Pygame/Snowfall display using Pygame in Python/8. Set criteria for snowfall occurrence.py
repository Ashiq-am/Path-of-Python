# loop till the close button is pressed
done = False

while not done:

# User did something
	for event in pygame.event.get():

	# If user clicked close
		if event.type == pygame.QUIT:

		# Flag that we are done so
		# we exit this loop
			done = True
