# define a function for
# collision detection
def crash():
    # take a global variable
    global blockYPosition

    # check conditions
    if playerYPosition < (blockYPosition + pixel):
        if ((playerXPosition > blockXPosition
		and playerXPosition < (blockXPosition + pixel))
		or ((playerXPosition + pixel) > blockXPosition
		and (playerXPosition + pixel) < (blockXPosition + pixel))):
            blockYPosition = height + 1000
