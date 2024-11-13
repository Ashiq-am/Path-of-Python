# Python3 program to implement
# the above approach
import sys


# Function to calculate the maximum
# possible sum by selecting X elements
# from the Matrix
def maxSum(grid):
    # Generate prefix sum of the matrix
    prefsum = [[0 for x in range(m)]
               for y in range(m)]

    for i in range(n):
        for x in range(m):
            if (x == 0):
                prefsum[i][x] = grid[i][x]
            else:
                prefsum[i][x] = (prefsum[i][x - 1] +
                                 grid[i][x])

    dp = [[-sys.maxsize - 1 for x in range(X + 1)]
          for y in range(n)]

    # Maximum possible sum by selecting
    # 0 elements from the first i rows
    for i in range(n):
        dp[i][0] = 0

    # If a single row is present
    for i in range(1, min(m, X)):
        dp[0][i] = (dp[0][i - 1] +
                    grid[0][i - 1])

    for i in range(1, n):
        for j in range(1, X + 1):

            # If elements from the
            # current row is not selected
            dp[i][j] = dp[i - 1][j]

            # Iterate over all possible
            # selections from current row
            for x in range(1, min(j, m) + 1):
                dp[i][j] = max(dp[i][j],
                               dp[i - 1][j - x] +
                               prefsum[i][x - 1])

    # Return maximum possible sum
    return dp[n - 1][X]


# Driver Code
if __name__ == "__main__":
    n = 4
    m = 4
    X = 6

    grid = [[3, 2, 6, 1],
            [1, 9, 2, 4],
            [4, 1, 3, 9],
            [3, 8, 2, 1]]
    ans = maxSum(grid)

    print(ans)
