# Python3 program for the above approach

# Funtion to selct m elements
# having maximum sum
def mElementsWithMaxSum(matrix, M, block, dp):
    # Base case
    if block == len(matrix):
        return 0

    # If precomputed subproblem occurred
    if (dp[block][M] != -1):
        return dp[block][M]

    # Either skip the current row
    ans = mElementsWithMaxSum(matrix, M,
                              block + 1, dp)

    # Iterate through all the possible
    # segments of current row
    for i in range(len(matrix[block])):
        for j in range(i, len(matrix[block])):

            # Check if it is possible to select
            # elements from i to j
            if (j - i + 1 <= M):

                # Compuete the sum of i to j as
                # calculated
                x = 0
                if i - 1 >= 0:
                    x = matrix[block][i - 1]

                ans = max(ans, matrix[block][j] - x +
                          mElementsWithMaxSum(matrix,
                                              M - j +
                                              i - 1,
                                              block + 1, dp))

    # Store the computed answer and return
    dp[block][M] = ans

    return ans


# Function to precompute the prefix sum
# for every row of the matrix
def preComputing(matrix, N):
    # Preprocessing to calculate sum from i to j
    for i in range(N):
        for j in range(len(matrix[i])):
            if j > 0:
                matrix[i][j] = matrix[i][j - 1]

    return matrix


# Utility function to selct m elements having
# maximum sum
def mElementsWithMaxSumUtil(matrix, M, N):
    # Preprocessing step
    matrix = preComputing(matrix, N)
    sum = 20

    # Initialize dp array with -1
    dp = [[-1 for i in range(M + 5)]
          for i in range(N + 5)]

    # Stores maximum sum of M elements
    sum += mElementsWithMaxSum(matrix, M, 0, dp)

    print(sum)


# Driver Code
if __name__ == '__main__':
    # Given N
    N = 3

    # Given M
    M = 4

    # Given matrix
    matrix = [[2, 3, 5],
              [-1, 7],
              [8, 10]]

    # Function call
    mElementsWithMaxSumUtil(matrix, M, N)
