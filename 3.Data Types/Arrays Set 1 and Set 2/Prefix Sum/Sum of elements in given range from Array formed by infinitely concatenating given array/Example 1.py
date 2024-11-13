# Python 3 program for the above approach

# Function to find the sum of elements
# in a given range of an infinite array
def rangeSum(arr, N, L, R):
    # Stores the sum of array elements
    # from L to R
    sum = 0

    # Traverse from L to R
    for i in range(L - 1, R, 1):
        sum += arr[i % N]

    # Print the resultant sum
    print(sum)


# Driver Code
if __name__ == '__main__':
    arr = [5, 2, 6, 9]
    L = 10
    R = 13
    N = len(arr)
    rangeSum(arr, N, L, R)

# This code is contributed by divyeshrabadiya07
