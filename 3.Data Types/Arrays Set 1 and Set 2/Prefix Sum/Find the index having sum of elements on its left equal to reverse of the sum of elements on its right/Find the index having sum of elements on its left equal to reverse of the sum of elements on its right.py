# Python3 Program to implement
# the above approach

# Function to check if a number is equal
# to the reverse of digits of other number
def checkReverse(leftSum, rightSum):
    # Stores reverse of
    # digits of rightSum
    rev = 0

    # Stores rightSum
    temp = rightSum

    # Calculate reverse of
    # digits of temp
    while (temp != 0):
        # Update rev
        rev = (rev * 10) + (temp % 10)

        # Update temp
        temp //= 10

    # If reverse of digits of
    # rightSum equal to leftSum
    if (rev == leftSum):
        return True

    return False


# Function to find the index
# that satisfies the condition
def findIndex(arr, N):
    # Stores sum of array elements
    # on right side of each index
    rightSum = 0

    # Stores sum of array elements
    # on left side of each index
    leftSum = 0

    # Traverse the array
    for i in range(N):
        # Update rightSum
        rightSum += arr[i]

    # Traverse the array
    for i in range(N):

        # Update rightSum
        rightSum -= arr[i]

        # If leftSum equal to
        # reverse of digits
        # of rightSum
        if (checkReverse(leftSum, rightSum)):
            return i

        # Update leftSum
        leftSum += arr[i]
    return -1


# Driver Code
if __name__ == '__main__':
    arr = [5, 7, 3, 6, 4, 9, 2]
    N = len(arr)
    print(findIndex(arr, N))
