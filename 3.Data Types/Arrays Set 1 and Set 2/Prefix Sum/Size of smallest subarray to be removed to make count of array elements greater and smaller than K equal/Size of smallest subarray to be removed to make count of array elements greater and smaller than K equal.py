# Python3 program to implement
# the above approach
import sys


# Function ot find the length
# of the smallest subarray
def smallSubarray(arr, n, total_sum):
    # Stores (prefix Sum, index)
    # as (key, value) mappings
    m = {}
    length = sys.maxsize
    prefixSum = 0

    # Iterate till N
    for i in range(n):

        # Update the prefixSum
        prefixSum += arr[i]

        # Update the length
        if (prefixSum == total_sum):
            length = min(length, i + 1)

        # Put the latest index to
        # find the minimum length
        m[prefixSum] = i

        if ((prefixSum - total_sum) in m.keys()):
            # Update the length
            length = min(length,
                         i - m[prefixSum - total_sum])

    # Return the answer
    return length


# Function to find the length of
# the largest subarray
def smallestSubarrayremoved(arr, n, k):
    # Stores the sum of all array
    # elements after modification
    total_sum = 0

    for i in range(n):

        # Change greater than k to 1
        if (arr[i] > k):
            arr[i] = 1

        # Change smaller than k to -1
        elif (arr[i] < k):
            arr[i] = -1

        # Change equal to k to 0
        else:
            arr[i] = 0

        # Update total_sum
        total_sum += arr[i]

    # No deletion required, return 0
    if (total_sum == 0):
        return 0
    else:

        # Delete smallest subarray
        # that has sum = total_sum
        return smallSubarray(arr, n,
                             total_sum)


# Driver Code
arr = [12, 16, 12, 13, 10]
K = 13

n = len(arr)

# Function call
print(smallestSubarrayremoved(arr, n, K))
