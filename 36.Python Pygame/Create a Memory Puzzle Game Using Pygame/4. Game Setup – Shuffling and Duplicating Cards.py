# Duplicate card images to create pairs
card_images *= 2

# Shuffle the cards
random.shuffle(card_images)

# Create a list to store the state of each card (True: face-up, False: face-down)
card_state = [False] * (GRID_SIZE ** 2)
