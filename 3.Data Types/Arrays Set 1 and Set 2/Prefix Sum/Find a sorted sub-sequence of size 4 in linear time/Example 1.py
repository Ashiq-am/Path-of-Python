# Python3 program for the above approach

# program to find a sorted
# sub-sequence of size 4
def findQuadruplet(arr, n):
    # If number of elements < 4
    # then no Quadruple are possible
    if (n < 4):
        print("No such Quadruple found")
        return

    flag = False

    # to check true or false
    # Index of greatest element
    # from right side
    max = n - 1

    # Index of smallest element
    # from left side
    min = 0

    # Index of second smallest element
    # from left side
    second_min = -1

    # Create another array that will
    # store index of a minimum element
    # on left side. If there is no minimum
    # element on left side,
    # then smaller[i] = -1
    smaller = [0] * n

    # Create another array that will
    # store index of a second minimum
    # element on left side. If there is no
    # second minimum element on left side,
    # then second_smaller[i] = -1
    second_smaller = [0] * n

    # First entry of both smaller and
    # second_smaller is -1.
    smaller[0] = -1
    second_smaller[0] = -1
    for i in range(1, n):
        if (arr[i] <= arr[min]):
            min = i
            smaller[0] = -1
            second_smaller[0] = -1

        else:
            smaller[i] = min
            if (second_min != -1):
                if (arr[second_min] < arr[i]):
                    second_smaller[i] = second_min

            else:
                second_smaller[i] = -1

            if (arr[i] < arr[second_min]
                    or second_min == -1):
                second_min = i

    # Create another array that will store
    # index of a greater element on right side.
    # If there is no greater element on
    # right side, then greater[i] = -1

    greater = [0] * n

    # Last entry of greater is -1.
    greater[n - 1] = -1
    for i in range(n - 2, -1, -1):
        if (arr[max] <= arr[i]):
            max = i
            greater[i] = -1

        else:
            greater[i] = max

    # Now we need to find a number which
    # has a greater on its right side and
    # two small on it's left side.
    for i in range(n):
        if (smaller[second_smaller[i]] != -1
                and second_smaller[i] != -1
                and greater[i] != -1):
            print("Quadruplets:", arr[smaller[second_smaller[i]]], end=" ")
            print(arr[second_smaller[i]], end=" ")
            print(arr[i], end=" ")
            print(arr[greater[i]])
            flag = True
            break
    if (flag == False):
        print("No such Quadruplet found")

    return


# Driver Code
arr = [1, 7, 4, 5, 3, 6]
N = len(arr)
findQuadruplet(arr, N)

# This code is contributed by sanjoy_62.
