# Python program for the above approach
import math


# Function to find maximum count of
# pairs of adjacent elements with even
# sum in the given circular array
def findMaximumPairs(arr):
    # Stores the value of current
    # integer during traversal
    currentElement = arr[0]
    count = 1

    # First chain's count and total number
    # of pairs is initially 0
    firstChainCount = 0
    totalPairs = 0

    # flag is used to check if the current
    # chain is the first chain in array
    flag = True;

    for i in range(1, len(arr)):

        # Count the number of
        # consecutive elements
        if (arr[i] == currentElement):
            count = count + 1

        else:
            if (flag == True):
                # Stores the count of
                # elements in 1st set
                firstChainCount = count
                flag = False

            # Update answer
            totalPairs = totalPairs + math.floor(count / 2)

            # Update current integer
            currentElement = arr[i]
            count = 1

    totalPairs = totalPairs + math.floor(count / 2)
    lastChainCount = count

    if (arr[0] == arr[len(arr) - 1]
            and firstChainCount % 2 == 1
            and lastChainCount % 2 == 1):
        totalPairs = totalPairs + 1

    # Print Answer
    print(totalPairs)


# Driver Code
arr = [1, 1, 1, 0, 1, 1, 0, 0]
findMaximumPairs(arr)
