# Python3 program for the above approach

# Function to find the starting index
# of the given circular array
# prefix sum array is non negative
import sys


def startingPoint(A, N):
    # Stores the sum of the array
    sum = 0

    # Stores the starting index
    startingindex = 0

    # Stores the minimum prefix
    # sum of A[0..i]
    min = sys.maxsize

    # Traverse the array
    for i in range(0, N):

        # Update the value of sum
        sum += A[i]

        # If sum is less than minimum
        if (sum < min):
            # Update the min as
            # the value of prefix sum
            min = sum

            # Update starting index
            startingindex = i + 1

    # Otherwise no such index is possible
    if (sum < 0):
        return -1

    return startingindex % N


# Driver code
arr = [3, -6, 7, -4, -4, 6, -1]
N = len(arr)

print(startingPoint(arr, N))
