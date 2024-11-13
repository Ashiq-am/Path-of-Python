# Python3 program for the above approach

# Function to find the maximum sum
# of a subsequence consisting of
# no K consecutive array elements
def Max_Sum(arr, K, N):
    # Stores states of dp
    dp = [0] * (N + 1)

    # Stores the prefix sum
    prefix = [None] * (N + 1)

    prefix[0] = 0

    # Update the prefix sum
    for i in range(1, N + 1):
        prefix[i] = prefix[i - 1] + arr[i - 1]

    # Base case for i < K
    dp[0] = 0

    # For indices less than k
    # take all the elements
    for i in range(1, K):
        dp[i] = prefix[i]

    # For i >= K case
    for i in range(K, N + 1):

        # Skip each element from i to
        # (i - K + 1) to ensure that
        # no K elements are consecutive
        for j in range(i, i - K, -1):
            # j-th element is skipped

            # Update the current dp state
            dp[i] = max(dp[i], dp[j - 1] +
                        prefix[i] - prefix[j])

    # dp[N] stores the maximum sum
    return dp[N]


# Driver Code
if __name__ == "__main__":
    # Given array arr[]
    arr = [4, 12, 22, 18, 34, 12, 25]

    N = len(arr)
    K = 5

    # Function call
    print(Max_Sum(arr, K, N))
