# // python program for the above approach

# // Function to find the factorial of
# // prefix sum at every possible index
def prefixFactorialArray(A, N):
    # // Find the prefix sum array
    for i in range(1, N):
        A[i] += A[i - 1]

    # // Stores the factorial of all the
    # // element till the sum of array
    fact = [0 for x in range(A[N - 1] + 1)]
    fact[0] = 1

    # // Find the factorial array
    for i in range(1, A[N - 1] + 1):
        fact[i] = i * fact[i - 1]

    # // Find the factorials of
    # // each array element
    for i in range(0, N):
        A[i] = fact[A[i]]

    # // Print the resultant array
    for i in range(0, N):
        print(A[i], end=" ")


# Driver code
arr = [1, 2, 3, 4]
N = len(arr)
prefixFactorialArray(arr, N)

# This code is contributed by amreshkumar3.
