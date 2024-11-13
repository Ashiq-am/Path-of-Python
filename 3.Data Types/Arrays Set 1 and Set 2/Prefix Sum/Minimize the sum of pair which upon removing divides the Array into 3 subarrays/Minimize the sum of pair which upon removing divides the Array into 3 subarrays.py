# Python 3 implementation of the above approach
import sys


# Function to find minimum possible sum
# of pair which breaks the array into 3
# non-empty subarrays
def minSumPair(arr, N):
    if (N < 5):
        return -1

    prefixMin = [0 for i in range(N)]
    prefixMin[0] = arr[0]

    # prefixMin[i] contains minimum element till i
    for i in range(1, N - 1, 1):
        prefixMin[i] = min(arr[i], prefixMin[i - 1])

    ans = sys.maxsize

    for i in range(3, N - 1, 1):
        ans = min(ans, arr[i] + prefixMin[i - 2])

    return ans


# Driver Code
if __name__ == '__main__':
    # Given array
    arr = [5, 2, 4, 6, 3, 7]
    N = len(arr)
    print(minSumPair(arr, N))

# This code is contributed by ipg201107.
