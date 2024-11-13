# Python program for the above approach

# Function to find the minimize
# replacements to make every element
# in the array A[] strictly greater
# than every element in B[] or vice-versa
def MinTime(a, b, n, m):
    # Store the final result
    ans = float('inf')

    # Create two arrays and
    # initialize with 0s
    prefix_a = [0] * 10
    prefix_b = [0] * 10

    # Traverse the array a[]
    for i in range(n):
        # Increment prefix_a[a[i]] by 1
        prefix_a[a[i]] += 1

    # Traverse the array b[]
    for i in range(m):
        # Increment prefix_b[b[i]] by 1
        prefix_b[b[i]] += 1

    # Calculate prefix sum
    # of the array a[]
    for i in range(1, 10):
        prefix_a[i] += prefix_a[i - 1]

    # Calculate prefix sum
    # of the array b[]
    for i in range(1, 10):
        prefix_b[i] += prefix_b[i - 1]

    # Iterate over the range [0, 9]
    for i in range(1, 10):
        # Make every element in array
        # a[] strictly greater than digit
        # i and make every element in the
        # array b[] less than digit i
        ans = min(ans, prefix_a[i] + m - prefix_b[i])

        # Make every element in array
        # b[] strictly greater than digit
        # i and make every element in
        # array a[] less than digit i
        ans = min(ans, n - prefix_a[i] + prefix_b[i])

    # Print the answer
    print(ans)


# Driver Code
A = [0, 0, 1, 3, 3]
B = [2, 0, 3]
N = len(A)
M = len(B)
MinTime(A, B, N, M)
