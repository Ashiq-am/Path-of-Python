def AddObstacles(obstacles0, obstacles1):
# Create an empty sprite group to store the combined obstacles
	obstacles = pygame.sprite.Group()

	# Add all obstacles from obstacles0 to the combined group
	for obstacle in obstacles0:
		obstacles.add(obstacle)

	# Add all obstacles from obstacles1 to the combined group
	for obstacle in obstacles1:
		obstacles.add(obstacle)

	return obstacles
