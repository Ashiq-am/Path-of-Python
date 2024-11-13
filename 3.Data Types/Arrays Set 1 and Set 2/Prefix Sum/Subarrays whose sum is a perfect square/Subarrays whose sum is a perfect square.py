# Python3 program to implement
# the above approach
import math


# Function to print the start and end
# indices of all subarrays whose sum
# is a perfect square
def PrintIndexes(arr, N):
    for i in range(N):

        # Stores the current
        # subarray sum
        currSubSum = 0

        for j in range(i, N, 1):

            # Update current subarray sum
            currSubSum += arr[j]

            # Stores the square root
            # of currSubSum
            sq = int(math.sqrt(currSubSum))

            # Check if currSubSum is
            # a perfect square or not
            if (sq * sq == currSubSum):
                print("(", i, ",",
                      j, ")", end=" ")


# Driver Code
arr = [65, 79, 81]
N = len(arr)

PrintIndexes(arr, N)
