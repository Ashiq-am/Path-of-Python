# Python3 program to find the length of
# the longest subarray whose sum is
# not divisible by integer

# Function to find the longest subarray
# with sum is not divisible by k
def MaxSubarrayLength(arr, n, k):
    # left is the index of the
    # leftmost element that is
    # not divisible by k
    left = -1

    # sum of the array
    sum = 0

    for i in range(n):

        # Find the element that
        # is not multiple of k
        if ((arr[i] % k) != 0):

            # left = -1 means we are
            # finding the leftmost
            # element that is not
            # divisible by k
            if (left == -1):
                left = i

            # Updating the
            # rightmost element
            right = i

        # Update the sum of the
        # array up to the index i
        sum += arr[i]

    # Check if the sum of the
    # array is not divisible
    # by k, then return the
    # size of array
    if ((sum % k) != 0):
        return n

    # All elements of array
    # are divisible by k,
    # then no such subarray
    # possible so return -1
    elif (left == -1):
        return -1

    else:

        # length of prefix elements
        # that can be removed
        prefix_length = left + 1

        # length of suffix elements
        # that can be removed
        suffix_length = n - right

        # Return the length of
        # subarray after removing
        # the elements which have
        # lesser number of elements
        return n - min(prefix_length,
                       suffix_length)


# Driver Code
if __name__ == "__main__":
    arr = [6, 3, 12, 15]
    n = len(arr)
    K = 3

    print(MaxSubarrayLength(arr, n, K))

# This code is contributed by chitranayal
