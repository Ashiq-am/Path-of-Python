# Python3 program for the above approach

# Function to count the number of subarrays
# of the given array having odd Bitwise XOR
def oddXorSubarray(a, n):
    # Stores number of odd
    # numbers upto i-th index
    odd = 0

    # Stores number of required
    # subarrays starting from i-th index
    c_odd = 0

    # Store the required result
    result = 0

    # Find the number of subarrays having odd
    # Bitwise XOR values starting at 0-th index
    for i in range(n):

        # Check if current element is odd
        if (a[i] & 1):
            odd = not odd

        # If the current value of odd is not
        # zero, increment c_odd by 1
        if (odd):
            c_odd += 1

    # Find the number of subarrays having odd
    # bitwise XOR value starting at ith index
    # and add to result
    for i in range(n):

        # Add c_odd to result
        result += c_odd
        if (a[i] & 1):
            c_odd = (n - i - c_odd)

    # Print the result
    print(result)


# Driver Code
if __name__ == '__main__':
    # Given array
    arr = [1, 4, 7, 9, 10]

    # Stores the size of the array
    N = len(arr)
    oddXorSubarray(arr, N)

# This code is contributed by mohit kumar 29.
