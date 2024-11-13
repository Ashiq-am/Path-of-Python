# Python3 program for the above approach

# Function to count array elements
# exceeding sum of preceding K elements
def countPrecedingK(a, n, K):
    prefix = [0] * n
    prefix[0] = a[0]

    # Iterate over the array
    for i in range(1, n):
        # Update prefix sum
        prefix[i] = prefix[i - 1] + a[i]

    ctr = 0

    # Check if arr[K] >
    # arr[0] + .. + arr[K - 1]
    if (prefix[K - 1] < a[K]):
        # Increment count
        ctr += 1

    for i in range(K + 1, n):

        # Check if arr[i] >
        # arr[i - K - 1] + .. + arr[i - 1]
        if (prefix[i - 1] -
                prefix[i - K - 1] < a[i]):
            # Increment count
            ctr += 1

    return ctr


# Driver Code
if __name__ == '__main__':
    # Given array
    arr = [2, 3, 8, 10, -2,
           7, 5, 5, 9, 15]

    N = len(arr)
    K = 2

    print(countPrecedingK(arr, N, K))
