# Python3 program to implement
# the above approach
N = int(1e5 + 5)
MOD = 1000000007
dp = [0] * N


# Function to calculate the
# count of possible strings
def countStrings(K, Q):
    # Initialize dp[0]
    dp[0] = 1

    # dp[i] represents count of
    # strings of length i
    for i in range(1, N):
        dp[i] = dp[i - 1]

        # Add dp[i-k] if i>=k
        if (i >= K):
            dp[i] = (dp[i] + dp[i - K]) % MOD

    # Update Prefix Sum Array
    for i in range(1, N):
        dp[i] = (dp[i] + dp[i - 1]) % MOD

    for i in range(len(Q)):
        ans = dp[Q[i][1]] - dp[Q[i][0] - 1]

        if (ans < 0):
            ans += MOD

        print(ans)


# Driver Code
K = 3

Q = [[1, 4], [3, 7]]

countStrings(K, Q)
