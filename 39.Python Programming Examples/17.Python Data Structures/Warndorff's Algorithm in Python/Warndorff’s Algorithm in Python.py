# Import necessary modules
import numpy as np

# Define the possible moves of a knight in chess
knight_moves = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]


def is_valid_move(x, y, board):
    """
    Check if the move is valid (within bounds and to an unvisited square).
    """
    return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == -1


def count_onward_moves(x, y, board):
    """
    Count the number of valid onward moves from the given position.
    """
    count = 0
    for move in knight_moves:
        next_x, next_y = x + move[0], y + move[1]
        if is_valid_move(next_x, next_y, board):
            count += 1
    return count


def warndorff_tour(board, curr_x, curr_y, move_count):
    """
    Perform the Knight's Tour using Warndorff's algorithm.
    """
    board[curr_x][curr_y] = move_count

    if move_count == len(board) * len(board[0]) - 1:
        return True

    # Get all possible moves from the current position
    next_moves = []
    for move in knight_moves:
        next_x, next_y = curr_x + move[0], curr_y + move[1]
        if is_valid_move(next_x, next_y, board):
            next_moves.append(
                (next_x, next_y, count_onward_moves(next_x, next_y, board)))

    # Sort moves based on the number of onward moves (Warndorff's heuristic)
    next_moves.sort(key=lambda x: x[2])

    # Try the moves in the order determined by Warndorff's heuristic
    for next_x, next_y, _ in next_moves:
        if warndorff_tour(board, next_x, next_y, move_count + 1):
            return True

    # Backtrack if no valid moves are found
    board[curr_x][curr_y] = -1
    return False


def knight_tour(size=8, start_x=0, start_y=0):
    """
    Initialize the chessboard and start the Knight's Tour from the given position.
    """
    board = np.full((size, size), -1)
    if warndorff_tour(board, start_x, start_y, 0):
        return board
    else:
        return None


# Example usage
if __name__ == "__main__":
    size = 8
    start_x, start_y = 0, 0
    tour_board = knight_tour(size, start_x, start_y)

    if tour_board is not None:
        print("Knight's Tour completed successfully:")
        print(tour_board)
    else:
        print("No solution found.")
