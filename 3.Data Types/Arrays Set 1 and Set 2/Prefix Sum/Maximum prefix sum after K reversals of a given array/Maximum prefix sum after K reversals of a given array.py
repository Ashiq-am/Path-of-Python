# Python3 program for the above approach
import sys


# Function to find the maximum prefix
# sum after K reversals of the array
def maxSumAfterKReverse(arr, K, N):
    # Stores the required sum
    sum = -sys.maxsize - 1

    # If K is odd, reverse the array
    if (K & 1):
        arr.reverse()

    # Store current prefix sum of array
    currsum = 0

    # Traverse the array arr[]
    for i in range(N):
        # Add arr[i] to currsum
        currsum += arr[i]

        # Update maximum prefix sum
        # till now
        sum = max(sum, currsum)

    # Prthe answer
    print(sum)


# Driver Code
arr = [1, 5, 8, 9, 11, 2]
K = 1
N = len(arr)

# Function Call
maxSumAfterKReverse(arr, K, N)
