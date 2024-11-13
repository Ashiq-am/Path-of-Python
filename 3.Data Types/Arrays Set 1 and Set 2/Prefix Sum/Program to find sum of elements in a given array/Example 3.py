# python Program to find sum of elements
# in a given array using recursion

# function to return sum of elements
# in an array of size n
def sum1(arr):

    if len(arr) == 1:
        return arr[0]

    else:
        return arr[0] + sum1(arr[1:])

arr = [12, 3, 4, 15]
print(sum1(arr))

# This code is contributed by laxmigangarajula03
