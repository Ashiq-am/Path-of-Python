# Python3 program for Split the array into three
# subarrays such that summation of first
# and third subarray is equal and maximum
import math


# Function to return the sum of
# the first subarray
def sumFirst(a, n):
    # Two pointers are initialized
    # one at the front and the other
    # at the back
    front_pointer = 0
    back_pointer = n - 1

    # prefixsum and suffixsum initialized
    prefixsum = a[front_pointer]
    suffixsum = a[back_pointer]

    # answer variable initialized to 0
    answer = 0

    while (front_pointer < back_pointer):

        # If the summation are equal
        if (prefixsum == suffixsum):

            # answer updated
            answer = max(answer, prefixsum)

            # Both the pointers are moved by step
            front_pointer += 1
            back_pointer -= 1

            # prefixsum and suffixsum are updated
            prefixsum += a[front_pointer]
            suffixsum += a[back_pointer]

        elif (prefixsum > suffixsum):

            # If prefixsum is more,then back pointer is
            # moved by one step and suffixsum updated.
            back_pointer -= 1
            suffixsum += a[back_pointer]
        else:

            # If prefixsum is less,then front pointer is
            # moved by one step and prefixsum updated.
            front_pointer += 1
            prefixsum += a[front_pointer]

    # answer is returned
    return answer


# Driver code
arr = [1, 3, 2, 1, 4]
n = len(arr)

# Function call
print(sumFirst(arr, n))
