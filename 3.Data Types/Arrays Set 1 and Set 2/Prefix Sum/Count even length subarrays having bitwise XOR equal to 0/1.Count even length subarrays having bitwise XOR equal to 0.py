# Python3 program to implement
# the above approach

# Function to count the number
# of even-length subarrays
# having Bitwise XOR equal to 0
def cntSubarr(arr, N):
    # Stores the count of
    # required subarrays
    res = 0

    # Stores prefix-XOR
    # of arr[i, i+1, ...N-1]
    prefixXor = 0

    # Traverse the array
    for i in range(N - 1):
        prefixXor = arr[i]
        for j in range(i + 1, N):

            # Calculate the prefix-XOR
            # of current subarray
            prefixXor ^= arr[j]

            # Check if XOR of the
            # current subarray is 0
            # and length is even
            if (prefixXor == 0 and
                    (j - i + 1) % 2 == 0):
                res += 1

    return res


# Driver Code
if __name__ == '__main__':
    arr = [2, 2, 3, 3, 6, 7, 8]
    N = len(arr)

    print(cntSubarr(arr, N))
