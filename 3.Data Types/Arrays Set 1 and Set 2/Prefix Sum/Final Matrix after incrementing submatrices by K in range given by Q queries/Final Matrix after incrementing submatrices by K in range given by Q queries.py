# Python3 program for the above approach

# Query data type

# Function to update the given query
def updateQuery(from_x, from_y,
                to_x, to_y, k, aux):
    # Update top cell
    aux[from_x][from_y] += k

    # Update bottom left cell
    if (to_x + 1 < 3):
        aux[to_x + 1][from_y] -= k

    # Update bottom right cell
    if (to_x + 1 < 3 and to_y + 1 < 4):
        aux[to_x + 1][to_y + 1] += k

    # Update top right cell
    if (to_y + 1 < 4):
        aux[from_x][to_y + 1] -= k


# return aux

# Function that updates the matrix
# mat[][] by adding elements of aux[][]
def updatematrix(mat, aux):
    # Compute the prefix sum of all columns
    for i in range(3):
        for j in range(1, 4):
            aux[i][j] += aux[i][j - 1]

    # Compute the prefix sum of all rows
    for i in range(4):
        for j in range(1, 3):
            aux[j][i] += aux[j - 1][i]

    # Get the final matrix by adding
    # mat and aux matrix at each cell
    for i in range(3):
        for j in range(4):
            mat[i][j] += aux[i][j]


# return mat

# Function that prints matrix mat[]
def printmatrix(mat):
    # Traverse each row
    for i in range(3):

        # Traverse each columns
        for j in range(4):
            print(mat[i][j], end=" ")

        print()


# Function that performs each query in
# the given matrix and prthe updated
# matrix after each operation performed
def matrixQuery(mat, Q, q):
    # Initialize all elements to 0
    aux = [[0 for i in range(4)]
           for i in range(3)]

    # Update auxiliary matrix
    # by traversing each query
    for i in range(Q):
        # Update Query
        updateQuery(q[i][0], q[i][1],
                    q[i][2], q[i][3],
                    q[i][4], aux)

    # Compute the final answer
    updatematrix(mat, aux)

    # Print the updated matrix
    printmatrix(mat)


# Driver Code
if __name__ == '__main__':
    # Given 4atrix
    mat = [[1, 0, 1, 2],
           [0, 2, 4, 1],
           [1, 2, 1, 0]]

    Q = 1

    # Given Queries
    q = [[0, 0, 1, 1, 2]]

    # Function Call
    matrixQuery(mat, Q, q)
