# Python 3 program to find subarray with
# sum closest to 0
import sys


# Function to find the subarray
def findSubArray(arr, n):
    min_sum = sys.maxsize

    # Pick a starting point
    for i in range(n):

        # Consider current starting point
        # as a subarray and update minimum
        # sum and subarray indexes
        curr_sum = arr[i]
        if (min_sum > abs(curr_sum)):
            min_sum = abs(curr_sum)
            start = i
            end = i

        # Try all subarrays starting with i
        for j in range(i + 1, n, 1):
            curr_sum = curr_sum + arr[j]

            # update minimum sum
            # and subarray indexes
            if (min_sum > abs(curr_sum)):
                min_sum = abs(curr_sum)
                start = i
                end = j

            # Return starting and ending indexes
    p = [start, end]
    return p


# Driver Code
if __name__ == '__main__':
    arr = [2, -5, 4, -6, -3]
    n = len(arr)

    point = findSubArray(arr, n)
    print("Subarray starting from ", end="")
    print(point[0], "to", point[1])
