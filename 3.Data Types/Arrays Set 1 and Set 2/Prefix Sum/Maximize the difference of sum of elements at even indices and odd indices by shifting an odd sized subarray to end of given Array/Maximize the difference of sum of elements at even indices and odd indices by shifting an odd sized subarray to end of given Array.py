# Python program for the above approach

# Function to find the maximum value of
# difference between sum of elements
# at even indices and sum of elements
# at odd indices by shifting
# a subarray of odd length to the
# end of the array
def find_maxsum(arr, n):
    prefix_sum = [0 for i in range(n + 1)]

    # Modify the array to keep
    # alternative +ve and -ve
    for i in range(n):
        if (i % 2 == 1):
            arr[i] = -arr[i]

    # Function to find the prefix sum
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

    # If n is even
    if (n % 2 == 0):

        # Initialize the maxval to -1e8
        maxval = -10 ** 8
        for i in range(1, n + 1):
            # If i is even (case-1)
            if (i % 2 == 0):
                maxval = max(maxval, 2 * prefix_sum[i] - prefix_sum[n])

            # If i is odd (case-2)
            else:
                maxval = max(maxval, 2 * prefix_sum[i - 1] - prefix_sum[n])

        # return the maxval
        return maxval

    else:
        # Initialize the maxval to -1e8
        maxval = -10 ** 8
        for i in range(1, n + 1):

            # If i is even (case 3)
            if (i % 2 == 0):
                maxval = max(maxval, 2 * prefix_sum[i - 1] - prefix_sum[n])

            # If i is odd (case 4)
            else:
                maxval = max(maxval, 2 * prefix_sum[i] - prefix_sum[n])

        # Return the maxval
        return maxval


# Initialize an array
arr = [1, 2, 3, 4, 5, 6]
N = len(arr)

# Function call
print(find_maxsum(arr, N))

# This code is contributed by Shubham Singh
