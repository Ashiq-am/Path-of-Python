# Boundaries to the Player

# if it comes at right end,
# stay at right end and
# does not exceed
if playerXPosition >= (width - pixel):
    playerXPosition = (width - pixel)

# if it comes at left end,
# stay at left end and
# does not exceed
if playerXPosition <= 0:
    playerXPosition = 0
