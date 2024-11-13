# Python program for the above approach

import math


# Function to find the float
# value of log function
def LOG(x, base):
    return int(math.log(x) / math.log(base))


# Function for finding the nearest
# power of X with respect to Y
def getNP(x, y):
    # Base Case
    if y == 1:
        return 1

    # Find the value of K
    k = int(math.log(x, y))

    # Nearest power of GCD closest to Y
    if abs(y ** k - x) < abs(y ** (k + 1) - x):
        return y ** k

    return y ** (k + 1)


# Function to find the GCD of a and b
def GCD(a, b):
    # Base Case
    if b == 0:
        return a

    # Recursively calculate GCD
    return GCD(b, a % b)


# Function to modify the given array
# such that each array element is the
# nearest power of X with respect to Y
def modifyEle(arr):
    # Stores the prefix GCD
    prevGCD = arr[0]

    # Traverse the array
    for i in range(1, len(arr)):
        # Find the current number
        NP = getNP(arr[i], prevGCD)

        # Update the GCD
        prevGCD = GCD(arr[i], prevGCD)

        # Update the array at the
        # current index
        arr[i] = NP

    # Return the updated GCD array
    return arr


# Driver Code
arr = [4, 2, 8, 2]

# Function Call
print(modifyEle(arr))
