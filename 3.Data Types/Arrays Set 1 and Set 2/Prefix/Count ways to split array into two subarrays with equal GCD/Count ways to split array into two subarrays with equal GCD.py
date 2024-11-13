# Python3 program to implement
# the above approach
import math


# Function to count number of ways to split
# array into two groups with equal GCD value.
def cntWaysToSplitArrayTwo(arr, N):
    # Stores prefix GCD
    # of the array
    prefixGCD = [0] * N

    # Update prefixGCD[0]
    prefixGCD[0] = arr[0]

    # Stores suffix GCD
    # of the array
    suffixGCD = [0] * N

    # Update suffixGCD[N - 1]
    suffixGCD[N - 1] = arr[N - 1]

    # Traverse the array
    for i in range(N):
        # Update prefixGCD[i]
        prefixGCD[i] = math.gcd(prefixGCD[i - 1], arr[i])

    # Traverse the array
    for i in range(N - 2, -1, -1):
        # Update prefixGCD[i]
        suffixGCD[i] = math.gcd(suffixGCD[i + 1], arr[i])

    # Stores count of ways to split array
    # into two groups with equal GCD
    cntWays = 0

    # Traverse prefixGCD[] and suffixGCD[]
    for i in range(N - 1):

        # If GCD of both groups equal
        if (prefixGCD[i] == suffixGCD[i + 1]):
            # Update cntWays
            cntWays += 1

    return cntWays


# Driver Code
arr = [8, 4, 4, 8, 12]
N = len(arr)

print(cntWaysToSplitArrayTwo(arr, N))

# This code is contributed by susmitakundugoaldanga
