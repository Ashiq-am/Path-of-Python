def createObstacles(s, e, num=10):
    # Create an empty sprite group to store the obstacles
    obstacles = pygame.sprite.Group()
    locations = []
    for i in range(num):
        # Generate random row and column indices within the specified range
        row = random.randint(s, e)
        col = random.randint(0, 9)

        # Calculate the obstacle's location based on the row and column indices
        location = [col * 64 + 20, row * 64 + 20]

        if location not in locations:
            locations.append(location)  # Add the location to the list to avoid duplicates
            # Distribute trees
            if i % 4 == 0:
                attribute = "tree"
            # Distribute stones
            elif i % 4 == 1:
                attribute = "stone"
            # Distribute flags
            else:
                attribute = "flag"

            # Get the image path corresponding to the attribute from the config module
            img_path = cfg.OBSTACLE_PATHS[attribute]

            # Create an obstacle instance with the determined attribute and add it to the group
            obstacle = ObstacleClass(img_path, location, attribute)
            obstacles.add(obstacle)

    return obstacles
