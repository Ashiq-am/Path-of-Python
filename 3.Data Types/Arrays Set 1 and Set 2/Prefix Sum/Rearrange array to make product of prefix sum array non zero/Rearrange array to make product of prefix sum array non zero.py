# Python3 program to implement
# the above approach

# Function to rearrange array
# that satisfies the given condition
def rearrangeArr(arr, N):
    # Stores sum of elements
    # of the given array
    totalSum = 0

    # Calculate totalSum
    for i in range(N):
        totalSum += arr[i]

    # If the totalSum is equal to 0
    if (totalSum == 0):

        # No possible way to
        # rearrange array
        print(-1)

    # If totalSum exceeds 0
    elif (totalSum > 0):

        # Rearrange the array
        # in descending order
        arr.sort(reverse=True)
        print(*arr, sep=' ')

    # Otherwise
    else:

        # Rearrange the array
        # in ascending order
        arr.sort()
        print(*arr, sep=' ')


# Driver Code
arr = [1, -1, -2, 3]
N = len(arr)

rearrangeArr(arr, N)


