# Python implementation to find the minimum
# absolute difference of the xor values
# of the two subarrays

import sys


# function to find the minimum absolute
# difference of the xor values of the
# two subarrays
def minDiffBtwXorValues(arr, n):
    # to store the xor value of the
    # entire array
    tot_xor = 0

    for i in range(n):
        tot_xor ^= arr[i]

    # 'part_xor' to store the xor value
    # of some subarray
    part_xor = 0
    min = sys.maxint

    for i in range(n - 1):

        # removing the xor value of the
        # subarray [0..i] form 'tot_xor',
        # i.e, it will contain the xor
        # value of the subarray [i+1..n-1]
        tot_xor ^= arr[i]

        # calculating the xor value of the
        # subarray [0..i]
        part_xor ^= arr[i]

        # if absolute difference is minimum,
        # then update 'min'
        if (abs(tot_xor - part_xor) < min):
            min = abs(tot_xor - part_xor)

        # required minimum absolute difference
    return min


# Driver program to test above
arr = [12, 6, 20, 14, 38, 6]
n = len(arr)
print("Minimum Absolute Difference =", minDiffBtwXorValues(arr, n))


