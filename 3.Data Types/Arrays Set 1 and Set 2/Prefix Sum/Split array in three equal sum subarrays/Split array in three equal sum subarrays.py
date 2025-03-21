# Python3 program to determine if array arr[]
# can be split into three equal sum sets.

# Function to determine if array arr[]
# can be split into three equal sum sets.
def findSplit(arr, n):
    # variable to store prefix sum
    preSum = 0

    # variables to store indices which
    # have prefix sum divisible by S/3.
    ind1 = -1
    ind2 = -1

    # variable to store sum of
    # entire array. S

    # Find entire sum of the array.
    S = arr[0]
    for i in range(1, n):
        S += arr[i]

    # Check if array can be split in
    # three equal sum sets or not.
    if (S % 3 != 0):
        return 0

    # Variables to store sum S/3
    # and 2*(S/3).
    S1 = S / 3
    S2 = 2 * S1

    for i in range(0, n):
        preSum += arr[i]

        # If prefix sum is equal to S/3
        # store current index.
        if (preSum == S1 and ind1 == -1):
            ind1 = i
        # If prefix sum is equal to 2*(S/3)
        # store current index.
        elif (preSum == S2 and ind1 != -1):
            ind2 = i

            # Come out of the loop as both the
            # required indices are found.
            break

    # If both the indices are found
    # then print them.
    if (ind1 != -1 and ind2 != -1):
        print("({}, {})".format(ind1, ind2))
        return 1

    # If indices are not found return 0.
    return 0


# Driver code
arr = [1, 3, 4, 0, 4]
n = len(arr)
if (findSplit(arr, n) == 0):
    print("-1")