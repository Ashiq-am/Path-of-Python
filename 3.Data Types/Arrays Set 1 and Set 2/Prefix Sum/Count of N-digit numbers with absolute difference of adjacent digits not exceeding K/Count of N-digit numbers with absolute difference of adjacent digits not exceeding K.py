# Python 3 Program to implement
# the above approach

# Function to return count
# of N-digit numbers with
# absolute difference of
# adjacent digits not
# exceeding K
def getCount(n, k):
    # For 1-digit numbers, the
    # count is 10
    if n == 1:
        return 10

    # dp[i][j] stores the count of
    # i-digit numbers ending with j
    dp = [[0 for x in range(11)]
          for y in range(n + 1)]

    # Initialize count for
    # 1-digit numbers
    for i in range(1, 10):
        dp[1][i] = 1

    # Compute values for count
    # of digits greater than 1
    for i in range(2, n + 1):
        for j in range(0, 10):
            # Find the range of allowed
            # numbers if last digit is j
            l = max(0, j - k)
            r = min(9, j + k)

            # Perform Range update
            dp[i][l] = dp[i][l] + dp[i - 1][j]
            dp[i][r + 1] = dp[i][r + 1] - dp[i - 1][j]

        # Prefix sum to find count of
        # of i-digit numbers ending with j
        for j in range(1, 10):
            dp[i][j] = dp[i][j] + dp[i][j - 1]

        # Stores the final answer
    count = 0

    for i in range(0, 10):
        count = count + dp[n][i]
    return count


# Driver Code
n, k = 2, 1
print(getCount(n, k))
