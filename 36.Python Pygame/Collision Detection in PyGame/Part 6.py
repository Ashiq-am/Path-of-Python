# Multiple Blocks Movement after each other
# and condition used because of game over function
if (blockYPosition >= height - 0 and
        blockYPosition <= (height + 200)):
    blockYPosition = 0 - pixel

# randomly assign value in range
blockXPosition = random.randint(0, (width - pixel))
