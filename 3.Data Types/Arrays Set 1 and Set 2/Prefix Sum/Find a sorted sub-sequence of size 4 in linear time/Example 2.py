# Python program to find a sorted
# sub-sequence of size 4
import sys


def findQuadruplet(arr, n):
    # If number of elements < 4
    # then no Quadruple are possible
    if (n < 4):
        print("No such Quadruple found")
        return

    # Initializing the variables with
    # INT_MAX macros.

    # To store the min element.
    small = sys.maxsize

    # To store the second minimum element.
    second_small = sys.maxsize

    # To store the middle element.
    mid = sys.maxsize

    # To remember the mid and the
    # minimum element.
    min = 0
    main_mid = 0
    main_min = 0

    # Traversing the array to find
    # the Quadruple
    for i in range(n):
        if (arr[i] <= small):
            small = arr[i]

        elif (arr[i] <= second_small):
            second_small = arr[i]
            min = small

        elif (arr[i] <= mid):
            mid = arr[i]
            main_mid = second_small
            main_min = min
        else:

            # If the number is greater than mid.
            print(f"Quadruplets: {main_min} {main_mid} {mid} {arr[i]}")

            # Return if Quadruple is found.
            return

    # If no Quadruple is found
    print("No such Quadruple")
    return


# Driver program
arr = [1, 7, 4, 5, 3, 6]
N = len(arr)
findQuadruplet(arr, N);

# This code is contributed by shinjanpatra
