# load the image
playerImage = pygame.image.load("player.png")

# set the position
playerXPosition = (width/2) - (pixel/2)

# So that the player will be
# at height of 20 above the base
playerYPosition = height - pixel - 10

# set initially 0
playerXPositionChange = 0

# define a function for setting
# the image at particular
# coordinates
def player(x, y):
    # paste image on screen object

    screen.blit(playerImage, (x, y))

    # load the image
    blockImage = pygame.image.load("rectangleBlock.png")

    # set the random position
    blockXPosition = random.randint(0,(width - pixel))


    blockYPosition = 0 - pixel

# set the speed of
# the block
blockXPositionChange = 0
blockYPositionChange = 2

# define a function for setting
# the image at particular
# coordinates
def block(x, y):
    # paste image on screen object
    screen.blit(blockImage, (x, y))
