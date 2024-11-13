# Function to find equilibrium point
# a: input array
# n: size of array
def equilibriumPoint(a, n):
    # Here we define two pointers to the array -> start =
    # 0, end = n-1 Two variables to take care of sum ->
    # left_sum = 0, right_sum = 0
    i, start, end, left_sum, right_sum = 0, 0, n - 1, 0, 0

    for i in range(n):

        # if the equilibrium element is found our start
        # will be equal to end variable and left_sum will
        # be equal right_sum => return the equilibrium
        # element
        if (start == end and right_sum == left_sum):
            return a[start]

        # if start is equal to end variable but left_sum is
        # not equal right_sum => no equilibrium element
        # return -1
        if (start == end):
            return -1

        # if left_sum > right_sum => add the current end
        # element to the right_sum and decrement end
        if (left_sum > right_sum):
            right_sum += a[end]
            end -= 1

        # if right_sum < left_sum => add the current start
        # element to the left_sum and increment start
        elif (right_sum > left_sum):
            left_sum += a[start]
            start += 1

        #	 if left_sum is equal right_sum but start is not
        # equal to end => we are still in the middle of
        # algorithm even though we found that left_sum is
        # equal right_sum we haven't got that one required
        # equilibrium element (So, in this case add the
        # current end element to the right_sum and
        # decrement end (or) add the current start element
        # to the left_sum and increment start, to make our
        # algorithm continue further)
        else:
            right_sum += a[end]
            end -= 1

    # When there is only one element in array our algorithm
    # exits without entering for loop So we can check if our
    # functions enters the loop if not we can directly
    # return the value as answer
    if (not i):
        return a[0]


# Driver code
arr = [2, 3, 4, 1, 4, 5]
size = len(arr)
print(equilibriumPoint(arr, size))

# This code is contributed by Shinjanpatra
