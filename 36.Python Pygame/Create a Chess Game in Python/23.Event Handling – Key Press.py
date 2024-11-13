# Handling key press events when the game is over
if event.type == pygame.KEYDOWN and game_over:
    # Check if the pressed key is the "Enter" key
    if event.key == pygame.K_RETURN:
        # Resetting the game state when the "Enter" key is pressed
        game_over = False
        winner = ''
        white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                        'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
        white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                           (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
        black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                        'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
        black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                           (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
        captured_pieces_white = []
        captured_pieces_black = []
        turn_step = 0
        selection = 100
        valid_moves = []
        # Update move options for both black and white
        black_options = check_options(black_pieces, black_locations, 'black')
        white_options = check_options(white_pieces, white_locations, 'white')
