# Python code to implement the approach

# Function to compute before matrix
def computeBeforeMatrix(N, M, after):
    # Declaring a 2d vector to store
    # the values of the before Matrix
    before = [[0 for i in range(M)] for j in range(N)]

    before[0][0] = after[0][0]
    for i in range(N):
        for j in range(M):
            if (i == 0 and j == 0):
                continue
            elif (i == 0):
                before[i][j] = after[i][j] - after[i][j - 1]
            elif (j == 0):
                before[i][j] = after[i][j] - after[i - 1][j]
            else:
                before[i][j] = after[i][j] + after[i - 1][j - 1] - after[i - 1][j] - after[i][j - 1]

        # Return the before[][] matrix
    return before


# Driver code

N, M = 2, 3
after = [[1, 3, 6], [3, 7, 11]]

# Function call
ans = computeBeforeMatrix(N, M, after)
for u in ans:
    for x in u:
        print(f"{x}", end=" ")
    print("")


