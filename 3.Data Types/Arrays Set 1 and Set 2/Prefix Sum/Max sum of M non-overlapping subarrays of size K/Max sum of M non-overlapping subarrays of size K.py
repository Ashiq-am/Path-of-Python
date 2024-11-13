# Python3 program to find Max sum of M non-overlapping
# subarray of size K in an Array

# calculating presum of array. presum[i]
# is going to store prefix sum of subarray
# of size k beginning with arr[i]
def calculatePresumArray(presum, arr, n, k):
    for i in range(k):
        presum[0] += arr[i]

    # store sum of array index i to i+k
    # in presum array at index i of it.
    for i in range(1, n - k + 1):
        presum[i] += presum[i - 1] + arr[i + k - 1] - arr[i - 1]

    # calculating maximum sum of m non overlapping array


def maxSumMnonOverlappingSubarray(presum, m, size, k, start):
    # if m is zero then no need any array
    # of any size so return 0.
    if (m == 0):
        return 0

    # if start is greater then the size
    # of presum array return 0.
    if (start > size - 1):
        return 0

    mx = 0

    # if including subarray of size k
    includeMax = presum[start] + maxSumMnonOverlappingSubarray(presum, m - 1, size, k, start + k)

    # if excluding element and searching
    # in all next possible subarrays
    excludeMax = maxSumMnonOverlappingSubarray(presum, m, size, k, start + 1)

    # return max
    return max(includeMax, excludeMax)


# Driver code
arr = [2, 10, 7, 18, 5, 33, 0]
n = len(arr)

m, k = 3, 1

presum = [0 for i in range(n + 1 - k)]
calculatePresumArray(presum, arr, n, k)

# resulting presum array will have a size = n+1-k
print(maxSumMnonOverlappingSubarray(presum, m, n + 1 - k, k, 0))
