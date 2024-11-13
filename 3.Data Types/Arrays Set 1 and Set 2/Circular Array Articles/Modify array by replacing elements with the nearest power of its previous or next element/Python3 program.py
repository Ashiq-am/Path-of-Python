# Python3 program for the above approach

import math


# Function to calculate the power
# of y which is nearest to x
def nearestPow(x, y):
    # Base Case
    if y == 1:
        return 1

    # Stores the logarithmic
    # value of x with base y
    k = int(math.log(x, y))

    if abs(y ** k - x) < abs(y ** (k + 1) - x):
        return y ** k

    return y ** (k + 1)


# Function to replace each array
# element by the nearest power of
# its previous or next element
def replacebyNearestPower(arr):
    # Stores the previous
    # and next element
    prev = arr[-1]

    lastNext = arr[0]

    # Traverse the array
    for i in range(len(arr)):

        temp = arr[i]
        if i == len(arr) - 1:
            next = lastNext
        else:
            next = arr[(i + 1) % len(arr)]

        # Calculate nearest power for
        # previous and next elements
        prevPow = nearestPow(arr[i], prev)
        nextPow = nearestPow(arr[i], next)

        # Replacing the array values
        if abs(arr[i] - prevPow) < abs(arr[i] - nextPow):
            arr[i] = prevPow
        else:
            arr[i] = nextPow
        prev = temp

    # Print the updated array
    print(arr)


# Driver Code

# Given array
arr = [2, 3, 4, 1, 2]

replacebyNearestPower(arr)
