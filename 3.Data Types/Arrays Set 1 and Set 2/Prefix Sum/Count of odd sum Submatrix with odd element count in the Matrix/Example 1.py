def oddSumOddElementCountSubmatrix(mat):
    # Size of given 2-D matrix
    n = len(mat)
    count = 0

    # Here we need all submatrix which
    # contains odd no. of element in them.
    # So all the matrix whose size is in
    # form 1*3, 1*5, 1*7, 3*1, 3*3, 3*5,
    # 3*7, 5*1, ... are valid submatrix
    # now we need to check for that sum
    # of element present in that
    # submatrix is odd or not

    # So this nested 4 for loop generates
    # all submatrix with size as
    # mentioned above
    for rsize in range(1, n + 1, 2):
        for csize in range(1, n + 1, 2):
            for row in range(n - rsize + 1):
                for col in range(n - csize + 1):
                    # Now do summation of
                    # element present in
                    # that subarray and if
                    # it's odd increment
                    # the count
                    subMatSum = 0
                    for i in range(row, row + rsize):
                        for j in range(col, col + csize):
                            subMatSum += mat[i][j]
                    if subMatSum % 2 == 1:
                        count += 1

    # Return answer
    return count


# Driver code
mat = [[1, 2, 3], [7, 5, 9], [6, 8, 10]]
print("Number of odd sum submatrices with odd number of elements: ", oddSumOddElementCountSubmatrix(mat))
