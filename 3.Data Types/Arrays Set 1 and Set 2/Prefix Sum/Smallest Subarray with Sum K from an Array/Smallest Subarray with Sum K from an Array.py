# Python3 program to implement
# the above approach
from collections import defaultdict
import sys


# Function to find the length of the
# smallest subarray with sum K
def subArraylen(arr, n, K):
    # Stores the frequency of
    # prefix sums in the array
    mp = defaultdict(lambda: 0)

    mp[arr[0]] = 0

    for i in range(1, n):
        arr[i] = arr[i] + arr[i - 1]
        mp[arr[i]] = i

    # Initialize ln
    ln = sys.maxsize

    for i in range(n):

        # If sum of array till i-th
        # index is less than K
        if (arr[i] < K):

            # No possible subarray
            # exists till i-th index
            continue
        else:

            # Find the exceeded value
            x = K - arr[i]

            # If exceeded value is zero
            if (x == 0):
                ln = min(ln, i)

            if (x in mp.keys()):
                continue
            else:
                ln = min(ln, i - mp[x])

    return ln


# Driver Code
arr = [1, 2, 4, 3, 2, 4, 1]
n = len(arr)

K = 7

ln = subArraylen(arr, n, K)

# Function call
if (ln == sys.maxsize):
    print("-1")
else:
    print(ln)
