# Python3 program for the above approach

# Function to determine if a given
# value can be median
def isMaximumMedian(arr, N, K, mid):
    # Stores the prefix sum array
    Pre = [[0 for x in range(N + 5)]
           for y in range(N + 5)]

    # Traverse the matrix arr[][]
    for i in range(N):
        for j in range(N):

            # Update Pre[i+1][j+1]
            Pre[i + 1][j + 1] = (Pre[i + 1][j] +
                                 Pre[i][j + 1] -
                                 Pre[i][j])

            # If arr[i][j] is less
            # than or equal to mid
            if (arr[i][j] <= mid):
                Pre[i + 1][j + 1] += 1

    # Stores the count of elements
    # should be less than mid
    required = (K * K + 1) // 2

    # Stores if the median mid
    # can be possible or not
    flag = 0

    # Iterate over the range [K, N]
    for i in range(K, N + 1):

        # Iterate over the range [K, N]
        for j in range(K, N + 1):

            # Stores count of elements less
            # than or equal to the value
            # mid in submatrix with bottom
            # right vertices at (i, j)
            X = (Pre[i][j] - Pre[i - K][j] -
                 Pre[i][j - K] + Pre[i - K][j - K])

            # If X is less than or
            # equal to required
            if (X < required):
                flag = 1

    # Return flag
    return flag


# Function to find the maximum median
# of a subsquare of the given size
def maximumMedian(arr, N, K):
    # Stores the range of the
    # search space
    low = 0
    high = 1000000009

    # Iterate until low is less
    # than high
    while (low < high):

        # Stores the mid value of
        # the range [low, high]
        mid = low + (high - low) // 2

        # If the current median can
        # be possible
        if (isMaximumMedian(arr, N, K, mid)):

            # Update the value of low
            low = mid + 1

        else:

            # Update the value of high
            high = mid

    # Return value stored in low as
    # answer
    return low


# Driver Code
if __name__ == "__main__":
    arr = [[1, 5, 12],
           [6, 7, 11],
           [8, 9, 10]]
    N = len(arr)
    K = 2

    print(maximumMedian(arr, N, K))

# This code is contributed by ukasp
