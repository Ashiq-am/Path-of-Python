# python program for the above approach

# Function to compute prefix sum
def find_prefixsum(M, N, arr, dp):
    # Assign 0 to first column
    for i in range(0, M + 1):
        dp[i][0] = 0

    # Assign 0 to first row
    for j in range(0, N + 1):
        dp[0][j] = 0

    # Iterate over the range
    # [1, M]
    for i in range(1, M + 1):

        # Iterate over the range
        # [1, N]
        for j in range(1, N + 1):
            dp[i][j] = dp[i][j - 1] + arr[i - 1][j - 1]

    # Iterate over the range
    # [1, M]
    for i in range(1, M + 1):

        # Iterate over the range
        # [1, N]
        for j in range(1, N + 1):
            # Update
            dp[i][j] = dp[i][j] + dp[i - 1][j]


# Function to find sub-squares
# with given sum S
def findSubsquares(arr, M, N, S):
    # Stores the prefix sum of
    # matrix
    dp = [[0 for i in range(N + 1)] for col in range(M + 1)]

    # Function call to find
    # prefix Sum of matrix
    find_prefixsum(M, N, arr, dp)

    # Stores the count of
    # subsquares with sum S
    cnt = 0
    for x in range(1, min(N, M)):

        # Iterate over every
        # element of the matrix
        for i in range(x, M + 1):
            for j in range(x, N + 1):

                # Stores the sum of
                # subsquare of dimension
                # x*x formed with i, j as
                # the bottom-right
                # vertex
                sum = dp[i][j] - dp[i - x][j] - dp[i][j - x] + dp[i - x][j - x]

                # If sum is equal to S

                if (sum == S):
                    # Increment cnt by 1
                    cnt += 1

    # Return the result
    return cnt


# Driver Code
# Input
M = 4
N = 5
arr = [[2, 4, 3, 2, 10],
       [3, 1, 1, 1, 5],
       [1, 1, 2, 1, 4],
       [2, 1, 1, 1, 3]]
S = 10

# Function call
print(findSubsquares(arr, M, N, S))
