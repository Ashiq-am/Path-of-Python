# Checking if bird is above the sealevel.
def isGameOver(horizontal, vertical, up_pipes, down_pipes):
    if vertical > elevation - 25 or vertical < 0:
        return True

    # Checking if bird hits the upper pipe or not
    for pipe in up_pipes:
        pipeHeight = game_images['pipeimage'][0].get_height()
        if (vertical < pipeHeight + pipe['y']
                and abs(horizontal - pipe['x']) < game_images['pipeimage'][0].get_width()):
            return True

    # Checking if bird hits the lower pipe or not
    for pipe in down_pipes:
        if (vertical + game_images['flappybird'].get_height() > pipe['y'])
            and abs(horizontal - pipe['x']) < game_images['pipeimage'][0].get_width():
        return True


return False
