# Python 3 program to find
# missing element from one array
# such that it has all elements
# of other array except
# one. Elements in two arrays
# can be in any order.

# This function mainly does XOR of all elements
# of arr1[] and arr2[]
def findMissing(arr1, arr2, M, N):
    if (M != N - 1 and N != M - 1):
        print("Invalid Input")
        return

    # Do XOR of all element
    res = 0
    for i in range(0, M):
        res = res ^ arr1[i]
    for i in range(0, N):
        res = res ^ arr2[i]

    print("Missing element is", res)


# Driver Code
arr1 = [4, 1, 5, 9, 7]
arr2 = [7, 5, 9, 4]
M = len(arr1)
N = len(arr2)
findMissing(arr1, arr2, M, N)
