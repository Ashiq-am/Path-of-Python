# Python3 code to generate all
# possible subsequences.
# Time Complexity O(n * 2 ^ n)
import math


def printSubsequences(arr, n):
    # Number of subsequences is (2**n -1)
    opsize = math.pow(2, n)

    # Run from counter 000..1 to 111..1
    for counter in range(1, (int)(opsize)):
        for j in range(0, n):

            # Check if jth bit in the counter
            # is set If set then print jth
            # element from arr[]
            if (counter & (1 << j)):
                print(arr[j], end=" ")

        print()


# Driver program
arr = [1, 2, 3, 4]
n = len(arr)
print("All Non-empty Subsequences")

printSubsequences(arr, n)


