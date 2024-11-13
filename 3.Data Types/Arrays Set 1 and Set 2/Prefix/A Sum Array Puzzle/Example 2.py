# Python3 implementation of above approach
def sumArray(arr, n):
    i, temp = 0, 0

    # Allocate memory for the sum array */
    Sum = [0 for i in range(n)]

    '''In this loop, temp variable contains
    sum of elements on left side excluding
    arr[i] '''
    for i in range(n):
        Sum[i] = temp
        temp += arr[i]

    # Initialize temp to 0 for sum
    # on right side */
    temp = 0

    ''' In this loop, temp variable contains
        sum of elements on right side excluding
        arr[i] */'''
    for i in range(n - 1, -1, -1):
        Sum[i] += temp
        temp += arr[i]

    for i in range(n):
        print(Sum[i], end=" ")


# Driver Code
arr = [3, 6, 4, 8, 9]
n = len(arr)
sumArray(arr, n)

# This code is contributed by
# Mohit Kumar 29
