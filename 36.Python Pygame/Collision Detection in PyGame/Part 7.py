# movement of Player
playerXPosition += playerXPositionChange

# movement of Block
blockYPosition += blockYPositionChange

# player Function Call
player(playerXPosition, playerYPosition)

# block Function Call
block(blockXPosition, blockYPosition)

# crash function call
crash()

# upadte screen
pygame.display.update()
