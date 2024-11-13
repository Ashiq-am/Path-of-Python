'''Python program to find
an index which has
same number of even
elements on left and
right, Or same number
of odd elements on
left and right.'''


# Function to find index
def findIndex(arr, n):
    for i in range(n):

        odd_left = 0
        even_left = 0
        odd_right = 0
        even_right = 0

        # To count Even and Odd
        # numbers of left side
        for j in range(i):
            if (arr[j] % 2 == 0):
                even_left = even_left + 1
            else:
                odd_left = odd_left + 1

        # To count Even and Odd
        # numbers of right side
        for k in range(n - 1, i, -1):
            if (arr[k] % 2 == 0):
                even_right = even_right + 1
            else:
                odd_right = odd_right + 1

        # To check Even Or Odd of Both
        # sides are equal or not
        if (even_right == even_left and odd_right == odd_left):
            return i

    return -1


# Driver's Function

arr = [4, 3, 2, 1, 2]
n = len(arr)
index = findIndex(arr, n)

if (index == -1):
    print("-1")
else:
    print("index = ", index)


