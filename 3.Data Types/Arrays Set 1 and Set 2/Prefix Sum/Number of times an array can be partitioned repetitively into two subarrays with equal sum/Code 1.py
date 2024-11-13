# Python3 program for the above approach

# Recursion Function to calculate the
# possible splitting
def splitArray(start, end, arr, prefix_sum):
    # If there are less than
    # two elements, we cannot
    # partition the sub-array.
    if (start >= end):
        return 0

    # Iterate from the start
    # to end-1.
    for k in range(start, end):
        if ((prefix_sum[k] - prefix_sum[start - 1]) ==
                (prefix_sum[end] - prefix_sum[k])):
            # Recursive call to the left
            # and the right sub-array.
            return (1 + splitArray(start, k, arr,
                                   prefix_sum) +
                    splitArray(k + 1, end, arr,
                               prefix_sum))

        # If there is no such partition,
    # then return 0
    return 0


# Function to find the total splitting
def solve(arr, n):
    # Prefix array to store
    # the prefix-sum using
    # 1 based indexing
    prefix_sum = [0] * (n + 1)

    prefix_sum[0] = 0

    # Store the prefix-sum
    for i in range(1, n + 1):
        prefix_sum[i] = (prefix_sum[i - 1] +
                         arr[i - 1])

    # Function Call to count the
    # number of splitting
    print(splitArray(1, n, arr, prefix_sum))


# Driver Code

# Given array
arr = [12, 3, 3, 0, 3, 3]
N = len(arr)

# Function call
solve(arr, N)
