# Python program to enlarge a matrix
# such that each element occurs in
# R rows and C columns

# Function to convert the matrix
# into a 1-D array
def oneD(matrix):
    # Variable to store the
    # given matrix
    m = []

    # Iterating through all the
    # elements of the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Adding the element into the
            # defined matrix
            m.append(matrix[i][j])

    return m[:]


# Function to enlarge a matrix
# such that each element occurs
# in R rows and C columns
def dimensions(R, C, matrix):
    # Initializing the enlarged
    # matrix
    ans = [[]] * R

    # Variables to iterate over
    # the matrix
    ctr = 0
    r = 0

    while (ctr < len(matrix)):

        # To keep the rows in the
        # range [0, R]
        r = r % R
        c = 0
        while (c < C):
            # In order to fix the number
            # of columns, the above r
            # statement can be commented
            # and this can be uncommented
            # c = c % C
            ans[r].append(matrix[ctr])

            c += 1

        ctr += 1
        r += 1

    return ans


# Driver code
if __name__ == '__main__':

    arr = [[1, 2], [3, 4]]
    R, C = 2, 3

    ans = dimensions(R, C, oneD(arr))

    # Print the enlarged matrix
    for i in ans:
        print(i)
