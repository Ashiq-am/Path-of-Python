# Python3 implementation to find the
# number of ways to cut the matrix
# into the K parts such that each
# part have atleast one filled cell

# Function to find the
# number of ways to cut the matrix
# into the K parts such that each
# part have atleast one filled cell
def ways(arr, k):
    R = len(arr)
    C = len(arr[0])
    K = k
    preSum = [[0 for _ in range(C)] \
              for _ in range(R)]

    # Loop to find prefix sum of the
    # given matrix
    for r in range(R - 1, -1, -1):
        for c in range(C - 1, -1, -1):
            preSum[r] = arr[r]

            if r + 1 < R:
                preSum[r] += preSum[r + 1]
            if c + 1 < C:
                preSum[r] += preSum[r]

            if r + 1 < R and c + 1 < C:
                preSum[r] -= preSum[r + 1]

    # dp(r, c, 1) = 1
    # if preSum[r] else 0
    dp = [[[0 for _ in range(C)] \
           for _ in range(R)] \
          for _ in range(K + 1)]

    # Loop to iterate over the dp
    # table of the given matrix
    for k in range(1, K + 1):
        for r in range(R - 1, -1, -1):
            for c in range(C - 1, -1, -1):
                if k == 1:
                    dp[k][r] = 1 \
                        if preSum[r] > 0 \
                        else 0
                else:
                    dp[k][r] = 0
                    for r1 in range(r + 1, R):

                        # Check if can cut horizontally
                        # at r1, at least one apple in
                        # matrix (r, c) -> r1, C-1
                        if preSum[r] - preSum[r1] > 0:
                            dp[k][r] += dp[k - 1][r1]
                    for c1 in range(c + 1, C):

                        # Check if we can cut vertically
                        # at c1, at least one apple in
                        # matrix (r, c) -> R-1, c1
                        if preSum[r] - preSum[r][c1] > 0:
                            dp[k][r] += dp[k - 1][r][c1]
    return dp[K][0][0]


# Driver Code
if __name__ == "__main__":
    arr = [[1, 0, 0], [1, 1, 1], [0, 0, 0]]
    k = 3

    # Function Call
    print(ways(arr, k))
