# Python3 program for the above approach

M = 6
N = 7


# Function to compute the matrix
# prefixCnt[M][N] from mat[M][N] such
# that prefixCnt[i][j] stores the
# count of 0's from (0, 0) to (i, j)
def preCompute(mat, prefixCnt):
    for i in range(M):

        for j in range(N):

            # Initialize prefixCnt[i][j]
            # with 1 if mat[i][j] is 0
            if (mat[i][j] == 0):
                prefixCnt[i][j] = 1

            # Otherwise, assign with 0
            else:
                prefixCnt[i][j] = 0

    # Calculate prefix sum for each row
    for i in range(M):
        for j in range(1, N):
            prefixCnt[i][j] += prefixCnt[i][j - 1]

    # Calculate prefix sum for each column
    for i in range(1, M):
        for j in range(N):
            prefixCnt[i][j] += prefixCnt[i - 1][j]
    return prefixCnt


# Function to compute count of 0's
# in submatrix from (pi, pj) to
# (qi, qj) from prefixCnt[M][N]
def countQuery(prefixCnt, pi, pj, qi, qj):
    # Initialize that count of 0's
    # in the sub-matrix within
    # indices (0, 0) to (qi, qj)
    cnt = prefixCnt[qi][qj]

    # Substract count of 0's within
    # indices (0, 0) and (pi-1, qj)
    if (pi > 0):
        cnt -= prefixCnt[pi - 1][qj]

    # Substract count of 0's within
    # indices (0, 0) and (qi, pj-1)
    if (pj > 0):
        cnt -= prefixCnt[qi][pj - 1]

    # Add prefixCnt[pi - 1][pj - 1]
    # because its value has been added
    # once but subtracted twice
    if (pi > 0 and pj > 0):
        cnt += prefixCnt[pi - 1][pj - 1]

    return cnt


# Function to count the 0s in the
# each given submatrix
def count0s(mat, Q, sizeQ):
    # Stores the prefix sum of each
    # row and column
    prefixCnt = [[0 for i in range(N)] for i in range(M)]

    # Compute matrix prefixCnt[][]
    prefixCnt = preCompute(mat, prefixCnt)

    for i in range(sizeQ):
        # Function Call for each query
        print(countQuery(prefixCnt, Q[i][0], Q[i][1], Q[i][2], Q[i][3]), end=" ")


# Driver Code
if __name__ == '__main__':
    # Given matrix
    mat = [[0, 1, 0, 1, 1, 1, 0],
           [1, 0, 1, 1, 1, 0, 1],
           [1, 1, 0, 0, 1, 1, 0],
           [1, 1, 1, 1, 1, 0, 1],
           [0, 0, 1, 0, 1, 1, 1],
           [1, 1, 0, 1, 1, 0, 1]]

    Q = [[0, 1, 3, 2],
         [2, 2, 4, 5],
         [4, 3, 5, 6]]

    sizeQ = len(Q)

    # Function Call
    count0s(mat, Q, sizeQ)
