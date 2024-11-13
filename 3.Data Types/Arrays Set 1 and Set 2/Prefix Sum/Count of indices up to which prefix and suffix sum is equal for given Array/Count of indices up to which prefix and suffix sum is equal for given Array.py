# Python implementation for the above approach

# Function to calculate number of
# equal prefix and suffix sums
# till the same indices
from builtins import range


def equalSumPreSuf(arr):
    # Initialize a variable
    # to store the result
    res = 0

    # Initialize variables to
    # calculate prefix and suffix sums
    preSum = 0
    sufSum = 0

    # Length of array arr
    length = len(arr)

    # Traverse the array from right to left
    for i in range(length - 1, -1, -1):
        # Add the current element
        # into sufSum
        sufSum += arr[i]

    # Iterate the array from left to right
    for i in range(length):

        # Add the current element
        # into preSum
        preSum += arr[i]

        # If prefix sum is equal to
        # suffix sum then increment res by 1
        if (preSum == sufSum):
            # Increment the result
            res += 1

        # Subtract the value of current
        # element arr[i] from suffix sum
        sufSum -= arr[i]

    # Return the answer
    return res


# Driver code
if __name__ == '__main__':
    # Initialize the array
    arr = [5, 0, 4, -1, -3, 0, 2, -2, 0, 3, 2]

    # Call the function and
    # prits result
    print(equalSumPreSuf(arr))


