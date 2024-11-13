def createPipe():
    offset = window_height / 3
    pipeHeight = game_images['pipeimage'][0].get_height()

    # generating random height of pipes
    y2 = offset + random.randrange(
        0, int(window_height - game_images['sea_level'].get_height() - 1.2 * offset))
    pipeX = window_width + 10
    y1 = pipeHeight - y2 + offset
    pipe = [

        # upper Pipe
        {'x': pipeX, 'y': -y1},

        # lower Pipe
        {'x': pipeX, 'y': y2}
    ]
    return pipe
