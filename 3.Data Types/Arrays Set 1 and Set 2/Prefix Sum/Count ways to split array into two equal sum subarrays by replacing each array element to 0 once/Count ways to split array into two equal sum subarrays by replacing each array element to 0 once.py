# Python3 program for the above approach

# Function to find number of ways to
# split array into 2 subarrays having
# equal sum by changing element to 0 once
def countSubArrayRemove(arr, N):
    # Stores the count of elements
    # in prefix and suffix of
    # array elements
    prefix_element_count = {}
    suffix_element_count = {}

    # Stores the sum of array
    total_sum_of_elements = 0

    # Traverse the array
    i = N - 1
    while (i >= 0):
        total_sum_of_elements += arr[i]

        # Increase the frequency of
        # current element in suffix
        suffix_element_count[arr[i]] = suffix_element_count.get(
            arr[i], 0) + 1

        i -= 1

    # Stores prefix sum upto index i
    prefix_sum = 0

    # Stores sum of suffix of index i
    suffix_sum = 0

    # Stores the desired result
    count_subarray_equal_sum = 0

    # Traverse the array
    for i in range(N):
        # Modify prefix sum
        prefix_sum += arr[i]

        # Add arr[i] to prefix map
        prefix_element_count[arr[i]] = prefix_element_count.get(
            arr[i], 0) + 1

        # Calculate suffix sum by
        # subtracting prefix sum
        # from total sum of elements
        suffix_sum = total_sum_of_elements - prefix_sum

        # Remove arr[i] from suffix map
        suffix_element_count[arr[i]] = suffix_element_count.get(
            arr[i], 0) - 1

        # Store the difference
        # between the subarrays
        difference = prefix_sum - suffix_sum

        # Count number of ways to split
        # the array at index i such that
        # subarray sums are equal
        number_of_subarray_at_i_split = (prefix_element_count.get(
            difference, 0) +
                                         suffix_element_count.get(
                                             -difference, 0))

        # Update the final result
        count_subarray_equal_sum += number_of_subarray_at_i_split

    # Return the result
    return count_subarray_equal_sum


# Driver Code
if __name__ == '__main__':
    arr = [1, 2, 1, 1, 3, 1]
    N = len(arr)

    # Function Call
    print(countSubArrayRemove(arr, N))
