# Python3 program for the above approach

import numpy as np


# Function to count ways to split
# an array into subarrays such that
# sum of the i-th subarray is
# divisible by i
def countOfWays(arr, N):
    # Stores the prefix sum of array
    pre = [0] * (N + 1);

    for i in range(N):
        # Find the prefix sum
        pre[i + 1] = pre[i] + arr[i];

    # Initialize dp[][] array
    dp = np.zeros((N + 2, N + 2));
    dp[1][0] += 1;

    # Stores the count of splitting
    ans = 0;

    # Iterate over the range [0, N]
    for i in range(N):
        for j in range(N, 0, -1):

            # Update the dp table
            dp[j + 1][pre[i + 1] % (j + 1)] += dp[j][pre[i + 1] % j];

            # If the last index is
            # reached, then add it
            # to the variable ans
            if (i == N - 1):
                ans += dp[j][pre[i + 1] % j];

    # Return the possible count of
    # splitting of array into subarrays
    return ans;


# Driver Code
if __name__ == "__main__":
    arr = [1, 2, 3, 4];
    N = len(arr);

    print(countOfWays(arr, N));

# This code is contributed by AnkThon
