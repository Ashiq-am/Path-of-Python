# Python program to count the number of
# rows and columns in a square matrix
# that contain repeated values

import numpy as np


# Function to count the number of rows
# and number of columns that contain
# repeated values in a square matrix.
def repeated_val(N, matrix):
    column = 0
    row = 0
    for i in range(N):

        # For every row, an array is formed.
        # The length of the unique elements
        # is calculated, which if not equal
        # to 'N' then the row has repeated values.
        if (len(np.unique(np.array(matrix[i]))) != N):
            row += 1

    # For every column, an array is formed.
    # The length of the unique elements
    # is calculated, which if not equal
    # to N then the column has repeated values.
    for j in range(N):
        if (len(np.unique(np.array([m[j] for m in matrix]))) != N):
            column += 1

    # Returning the count of
    # rows and columns
    return row, column


# Driver code
if __name__ == '__main__':
    N = 3
    matrix = [[2, 1, 3], [1, 3, 2], [1, 2, 3]]

    print(repeated_val(N, matrix))
