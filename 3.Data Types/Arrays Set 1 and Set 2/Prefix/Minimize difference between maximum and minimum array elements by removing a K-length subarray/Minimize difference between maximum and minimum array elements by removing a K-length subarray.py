# Python 3 program for the above approach

# Function to minimize difference
# between maximum and minimum array
# elements by removing a K-length subarray
def minimiseDifference(arr, K):
    # Size of array
    N = len(arr)

    # Stores the maximum and minimum
    # in the suffix subarray [i .. N-1]
    maxSuffix = [0 for i in range(N + 1)]
    minSuffix = [0 for i in range(N + 1)]

    maxSuffix[N] = -1e9
    minSuffix[N] = 1e9
    maxSuffix[N - 1] = arr[N - 1]
    minSuffix[N - 1] = arr[N - 1]

    # Constructing the maxSuffix and
    # minSuffix arrays

    # Traverse the array
    i = N - 2
    while (i >= 0):
        maxSuffix[i] = max(maxSuffix[i + 1], arr[i])
        minSuffix[i] = min(minSuffix[i + 1], arr[i])
        i -= 1

    # Stores the maximum and minimum
    # in the prefix subarray [0 .. i-1]
    maxPrefix = arr[0]
    minPrefix = arr[0]

    # Store the minimum difference
    minDiff = maxSuffix[K] - minSuffix[K]

    # Traverse the array
    for i in range(1, N):

        # If the suffix doesn't exceed
        # the end of the array
        if (i + K <= N):
            # Store the maximum element
            # in array after removing
            # subarray of size K
            maximum = max(maxSuffix[i + K], maxPrefix)

            # Stores the maximum element
            # in array after removing
            # subarray of size K
            minimum = min(minSuffix[i + K], minPrefix)

            # Update minimum difference
            minDiff = min(minDiff, maximum - minimum)

        # Updating the maxPrefix and
        # minPrefix with current element
        maxPrefix = max(maxPrefix, arr[i])
        minPrefix = min(minPrefix, arr[i])

    # Print the minimum difference
    print(minDiff)


# Driver Code
if __name__ == '__main__':
    arr = [4, 5, 8, 9, 1, 2]
    K = 2
    minimiseDifference(arr, K)

# This code is contributed by SURENDRA_GANGWAR.
