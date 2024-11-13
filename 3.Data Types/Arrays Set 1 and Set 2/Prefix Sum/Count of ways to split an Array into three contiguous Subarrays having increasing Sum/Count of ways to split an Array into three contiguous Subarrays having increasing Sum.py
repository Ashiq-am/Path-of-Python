# Python3 program to implement
# the above approach

# Function to count the number of ways
# to split array into three contigous
# subarrays of the required type
def findCount(arr, n):
    # Stores the prefix sums
    prefix_sum = [0 for x in range(n)]
    prefix_sum[0] = arr[0]

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]

    # Stores the suffix sums
    suffix_sum = [0 for x in range(n)]

    suffix_sum[n - 1] = arr[n - 1]

    for i in range(n - 2, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + arr[i]

    s = 1
    e = 1
    curr_subarray_sum = 0
    count = 0

    # Traverse the given array
    while (s < n - 1 and e < n - 1):

        # Updating curr_subarray_sum until
        # it is less than prefix_sum[s-1]
        while (e < n - 1 and
               curr_subarray_sum < prefix_sum[s - 1]):
            curr_subarray_sum += arr[e]
            e += 1

        if (curr_subarray_sum <= suffix_sum[e]):
            # Increase count
            count += 1

        # Decrease curr_subarray_sum by arr[s[]
        curr_subarray_sum -= arr[s]
        s += 1

    # Return count
    return count


# Driver code
arr = [2, 3, 1, 7]
n = len(arr)

print(findCount(arr, n))
