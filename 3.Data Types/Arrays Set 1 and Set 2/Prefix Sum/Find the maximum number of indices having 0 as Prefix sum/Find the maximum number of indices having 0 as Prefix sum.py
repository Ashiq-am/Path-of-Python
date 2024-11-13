# Python code for the above approach

# Function to find maximum 0 prefix sums
# after replacing 0's
def findmax_zeroprefixes(arr, n):
    # Initialize the arrays say prefix_sum
    # to store the prefix sum and the array
    # end mark to the mark array to mark
    # the end of subarray starting with 0.
    prefix_sum = [0] * n

    endmark = [True] * n

    # Initialize the variables flag to
    # check whether 0 as occured before
    # and max_freq to store the maximum
    # frequency of prefix sums of each
    # subarray and res to store max
    # possible 0 prefix sums.
    flag = 0
    max_freq = 0
    res = 0

    if (arr[0] == 0):
        flag = 1

    # Traverse through the the array and mark
    # the end of subarray staring with 0.
    for i in range(n):
        if (i + 1 < n):
            if (arr[i + 1] == 0):
                endmark[i] = True
            else:
                endmark[i] = False
        else:
            endmark[i] = True

    # Build the prefix sum array
    # of the array arr[]
    prefix_sum[0] = arr[0];
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]

    res = 0

    # Initialize a map to store
    # the frequencies
    freq = {}
    max_freq = 0

    # Iterate through the array and add
    # the frequency of most frequent
    # prefix sum of each subarray
    # starting with 0 to the res.
    for i in range(n):
        # If endmark of that index is false
        # keep the frequency of prefix sum
        # at that index increasing
        if (endmark[i] == False):
            if (prefix_sum[i] in freq):
                freq[prefix_sum[i]] = freq[prefix_sum[i]] + 1
            else:
                freq[prefix_sum[i]] = 1
            max_freq = max(max_freq, freq[prefix_sum[i]])

        # Else add the maximum frequent
        # prefix sum to the res.
        else:
            if (prefix_sum[i] in freq):
                freq[prefix_sum[i]] = freq[prefix_sum[i]] + 1
            else:
                freq[prefix_sum[i]] = 1

            max_freq = max(max_freq, freq[prefix_sum[i]])

            # For the first subarray whose
            # sum is 0
            if (flag == 0):
                # Add the frequency of
                # zero prefixsums
                if (0 in freq):
                    res = res + freq[0]
                max_freq = 0
                freq.clear()
                flag = 1
            # For the remaining subarrays starting
            # with 0's
            else:
                # Add the max frequency
                res = res + max_freq
                freq.clear()
                max_freq = 0
    # Return the res
    return res


# Driver function
arr = [2, 0, 1, -1, 0]
n = len(arr)
print(findmax_zeroprefixes(arr, n))

# This code is contributed by Pushpesh Raj.
