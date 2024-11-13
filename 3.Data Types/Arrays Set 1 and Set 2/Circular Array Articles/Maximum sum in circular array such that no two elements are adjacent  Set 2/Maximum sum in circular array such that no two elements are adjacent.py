# Python3 program to find maximum sum
# in circular array such that
# no two elements are adjacent

# Store the maximum possible at each index
dp = []


def maxSum(i, subarr):
    # When i exceeds the index of the
    # last element simply return 0
    if (i >= len(subarr)):
        return 0

    # If the value has already been
    # calculated, directly return
    # it from the dp array
    if (dp[i] != -1):
        return dp[i]

    # The next states are don't take
    # this element and go to (i + 1)th state
    # else take this element
    # and go to (i + 2)th state
    dp[i] = max(maxSum(i + 1, subarr),
                subarr[i] +
                maxSum(i + 2, subarr))
    return dp[i]


# function to find the max value
def Func(arr):
    subarr = arr

    # subarr contains elements
    # from 0 to arr.size() - 2
    subarr.pop()
    global dp

    # Initializing all the values with -1
    dp = [-1] * (len(subarr))

    # Calculating maximum possible
    # sum for first case
    max1 = maxSum(0, subarr)

    subarr = arr

    # subarr contains elements
    # from 1 to arr.size() - 1
    subarr = subarr[:]

    del dp

    # Re-initializing all values with -1
    dp = [-1] * (len(subarr))

    # Calculating maximum possible
    # sum for second case
    max2 = maxSum(0, subarr)

    # Printing the maximum between them
    print(max(max1, max2))


# Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 1]
    Func(arr)
