# Python3 implementation of the approach

# Function to print the arrangement that
# satisifes the given condition
def printArrangement(a, n):
    # Sort the array initially
    a = sorted(a)

    # Array that stores the arrangement
    b = [0 for i in range(n)]

    # Once the array is sorted
    # Re-fill the array again in the
    # mentioned way in the approach
    low = 0
    high = n - 1
    for i in range(n):
        if (i % 2 == 0):
            b[low] = a[i]
            low += 1
        else:
            b[high] = a[i]
            high -= 1

    # Iterate in the array
    # and check if the arrangement made
    # satisfies the given condition or not
    for i in range(n):

        # For the first element
        # the adjacents will be a[1] and a[n-1]
        if (i == 0):
            if (b[n - 1] + b[1] <= b[i]):
                print("-1")
                return

        # For the last element
        # the adjacents will be a[0] and a[n-2]
        elif (i == (n - 1)):
            if (b[n - 2] + b[0] <= b[i]):
                print("-1")
                return

        else:
            if (b[i - 1] + b[i + 1] <= b[i]):
                print("-1")
                return

    # If we reach this position then
    # the arrangement is possible
    for i in range(n):
        print(b[i], end=" ")

    # Driver code


a = [1, 4, 4, 3, 2]
n = len(a)

printArrangement(a, n)
