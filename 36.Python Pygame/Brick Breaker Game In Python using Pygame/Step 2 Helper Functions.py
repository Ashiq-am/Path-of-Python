# Helper Functions

# Function used to check collisions between any two entities
def collisionChecker(rect, ball):
    if pygame.Rect.colliderect(rect, ball):
        return True

    return False


# Function used to populate the blocks
def populateBlocks(blockWidth, blockHeight, horizontalGap, verticalGap):
    listOfBlocks = []

    for i in range(0, WIDTH, blockWidth + horizontalGap):
        for j in range(0, HEIGHT // 2, blockHeight + verticalGap):
            listOfBlocks.append(Block(i, j, blockWidth,
                                      blockHeight,
                                      random.choice([WHITE, GREEN])))

    return listOfBlocks


# Once all the lives are over, this function waits
# until exit or space bar is pressed and does the
# corresponding action
def gameOver():
    gameOver = True

    while gameOver:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
