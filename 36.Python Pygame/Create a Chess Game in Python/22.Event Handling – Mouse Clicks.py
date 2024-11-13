# event handling
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False
    # Handling left mouse button clicks when the game is not over
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
        x_coord = event.pos[0] // 100
        y_coord = event.pos[1] // 100
        click_coords = (x_coord, y_coord)
        # Handling player input during the first two turns
        if turn_step <= 1:
            # Check if the player clicked on forfeit squares
            if click_coords == (8, 8) or click_coords == (9, 8):
                winner = 'black'
            # Check if the clicked coordinates belong to white pieces
            if click_coords in white_locations:
                selection = white_locations.index(click_coords)
                if turn_step == 0:
                    turn_step = 1
            # Check if the clicked coordinates are valid moves for the selected white piece
            if click_coords in valid_moves and selection != 100:
                white_locations[selection] = click_coords
                # Check for capturing black pieces
                if click_coords in black_locations:
                    black_piece = black_locations.index(click_coords)
                    captured_pieces_white.append(black_pieces[black_piece])
                    if black_pieces[black_piece] == 'king':
                        winner = 'white'
                    black_pieces.pop(black_piece)
                    black_locations.pop(black_piece)
                # Update move options for both black and white
                black_options = check_options(
                    black_pieces, black_locations, 'black')
                white_options = check_options(
                    white_pieces, white_locations, 'white')
                turn_step = 2
                selection = 100
                valid_moves = []
        # Handling player input during the last two turns
        if turn_step > 1:
            # Check if the player clicked on forfeit squares
            if click_coords == (8, 8) or click_coords == (9, 8):
                winner = 'white'
            # Check if the clicked coordinates belong to black pieces
            if click_coords in black_locations:
                selection = black_locations.index(click_coords)
                if turn_step == 2:
                    turn_step = 3
            # Check if the clicked coordinates are valid moves for the selected black piece
            if click_coords in valid_moves and selection != 100:
                black_locations[selection] = click_coords
                # Check for capturing white pieces
                if click_coords in white_locations:
                    white_piece = white_locations.index(click_coords)
                    captured_pieces_black.append(white_pieces[white_piece])
                    if white_pieces[white_piece] == 'king':
                        winner = 'black'
                    white_pieces.pop(white_piece)
                    white_locations.pop(white_piece)
                # Update move options for both black and white
                black_options = check_options(
                    black_pieces, black_locations, 'black')
                white_options = check_options(
                    white_pieces, white_locations, 'white')
                turn_step = 0
                selection = 100
                valid_moves = []
