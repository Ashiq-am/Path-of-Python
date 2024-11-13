# Python 3 program to find floor value
# of mean in range l to r
import math


# To find mean of range in l to r
def findMean(arr, l, r):
    # Both sum and count are
    # initialize to 0
    sum, count = 0, 0

    # To calculate sum and number
    # of elements in range l to r
    for i in range(l, r + 1):
        sum += arr[i]
        count += 1

    # Calculate floor value of mean
    mean = math.floor(sum / count)

    # Returns mean of array
    # in range l to r
    return mean


# Driver Code
arr = [1, 2, 3, 4, 5]

print(findMean(arr, 0, 2))
print(findMean(arr, 1, 3))
print(findMean(arr, 0, 4))
