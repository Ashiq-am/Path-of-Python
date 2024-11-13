# Python3` program for the above approach

# Function to find the largest sum
# pair that are K distant apart
def getMaxPairSum(arr, N, K):
    # Stores the prefix maximum array
    preMax = [0] * N

    # Base Case
    preMax[0] = arr[0]

    # Traverse the array and update
    # the maximum value upto index i
    for i in range(1, N):
        preMax[i] = max(preMax[i - 1], arr[i])

    # Stores the maximum sum of pairs
    res = -10 ** 8

    # Iterate over the range [K, N]
    for i in range(K, N):
        # Find the maximum value of
        # the sum of valid pairs
        res = max(res, arr[i] + preMax[i - K])

    # Return the resultant sum
    return res


# Driver Code
if __name__ == '__main__':
    arr = [1, 2, 4, 8, 6, 3]
    K = 3
    N = len(arr)
    print(getMaxPairSum(arr, N, K))

# This code is contributed by mohit kumar 29.
