running = True

while running:
    # set the image on screen object
    screen.blit(backgroundImg, (0, 0))

# loop through all events
for event in pygame.event.get():

    # check the quit condition
    if event.type == pygame.QUIT:
        # quit the game
        pygame.quit()

    # movement key control of player
    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_RIGHT:
            playerXPositionChange = 3

        if event.key == pygame.K_LEFT:
            playerXPositionChange = -3

    if event.type == pygame.KEYUP:

        if event.key == pygame.K_RIGHT or pygame.K_LEFT:
            playerXPositionChange = 0
