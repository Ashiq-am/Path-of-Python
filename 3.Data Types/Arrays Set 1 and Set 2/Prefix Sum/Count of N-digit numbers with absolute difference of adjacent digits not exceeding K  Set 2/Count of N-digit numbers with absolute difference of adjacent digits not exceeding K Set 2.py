# Python3 program to implement
# the above approach

# Function to return the count
# of such numbers
def getCount(n, K):
    # For 1-digit numbers, the count
    # is 10 irrespective of K
    if (n == 1):
        return 10

    # dp[j] stores the number
    # of such i-digit numbers
    # ending with j
    dp = [0] * 11

    # Stores the results of length i
    next = [0] * 11

    # Initialize count for
    # 1-digit numbers
    for i in range(1, 9 + 1):
        dp[i] = 1

    # Compute values for count of
    # digits greater than 1
    for i in range(2, n + 1):
        for j in range(9 + 1):
            # Find the range of allowed
            # numbers if last digit is j
            l = max(0, j - k)
            r = min(9, j + k)

            # Perform Range update
            next[l] += dp[j]
            next[r + 1] -= dp[j]

        # Prefix sum to find actual count
        # of i-digit numbers ending with j
        for j in range(1, 9 + 1):
            next[j] += next[j - 1]

        # Update dp[]
        for j in range(10):
            dp[j] = next[j]
            next[j] = 0

    # Stores the final answer
    count = 0
    for i in range(9 + 1):
        count += dp[i]

    # Return the final answer
    return count


# Driver code
if __name__ == '__main__':
    n = 2
    k = 1

    print(getCount(n, k))
