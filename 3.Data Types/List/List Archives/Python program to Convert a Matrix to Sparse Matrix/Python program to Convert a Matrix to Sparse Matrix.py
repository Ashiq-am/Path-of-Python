# Python program to convert a
# matrix to sparse matrix


# function display a matrix
def displayMatrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

    # function to convert the matrix


# into a sparse matrix
def convertToSparseMatrix(matrix):
    # creating an empty sparse
    # matrix list
    sparseMatrix = []

    # searching values greater
    # than zero
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                # creating a temporaray
                # sublist
                temp = []

                # appending row value, column
                # value and element into the
                # sublist
                temp.append(i)
                temp.append(j)
                temp.append(matrix[i][j])

                # appending the sublist into
                # the sparse matrix list
                sparseMatrix.append(temp)

            # displaying the sparse matrix
    print("\nSparse Matrix: ")
    displayMatrix(sparseMatrix)


# Driver's code
# initializing a normal matrix
normalMatrix = [[1, 0, 0, 0],
                [0, 2, 0, 0],
                [0, 0, 3, 0],
                [0, 0, 0, 4],
                [5, 0, 0, 0]]

# displaying the matrix
displayMatrix(normalMatrix)

# converting the matrix to sparse
# displayMatrix
convertToSparseMatrix(normalMatrix)
