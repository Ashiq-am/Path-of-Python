# Move the snowFall down one pixel
snowFall[i][1] += 1

# If the snowFall has moved off the bottom of the screen
if snowFall[i][1] > 400:
    # Reset it just above the top
    y = random.randrange(-50, -10)
    snowFall[i][1] = y

    # Give it a new x position
    x = random.randrange(0, 400)
    snowFall[i][0] = x

# Go ahead and update the screen with what we've drawn.
pygame.display.flip()
clock.tick(20)
pygame.quit()
