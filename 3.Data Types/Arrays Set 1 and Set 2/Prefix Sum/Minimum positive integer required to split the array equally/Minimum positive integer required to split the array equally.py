# Python 3 program to find the minimum
# non-negative element required to split
# the array into two subarrays with equal sum
import sys


# Function to return the minimum positive
# integer required to split array into two
# subarrays with equal sums
def findMinimumSplit(arr, n):
    # Find the sum of whole array
    totalSum = 0
    for i in range(n):
        totalSum += arr[i]

    # leftSubarraySum stores the sum of
    # arr[0....i] and rightSubarraySum
    # stores the sum of arr[i + 1....n]
    leftSubarraySum = 0
    rightSubarraySum = 0
    minimumElement = sys.maxsize

    for i in range(n - 1):

        # Find the left subarray sum and
        # corresponding right subarray sum
        leftSubarraySum += arr[i]
        rightSubarraySum = totalSum - leftSubarraySum

        # if left subarray has larger sum, find the
        # element to be included in the right
        # subarray to make their sums equal
        if (leftSubarraySum > rightSubarraySum):
            element = leftSubarraySum - rightSubarraySum
            if (element < minimumElement):
                minimumElement = element

            # the Right subarray has larger sum,
        # find the element to be included in
        # the left subarray to make their sums equal
        else:
            element = rightSubarraySum - leftSubarraySum
            if (element < minimumElement):
                minimumElement = element

    return minimumElement


# Driver Code
if __name__ == "__main__":

    arr = [3, 2, 1, 5, 7, 8]
    n = len(arr)

    minimumElement = findMinimumSplit(arr, n)

    # If 0 then no insertion is required
    if (minimumElement == 0):
        print("No Extra Element Required")

    else:
        print(minimumElement)


