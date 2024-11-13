# Python code to implement the approach

# Function to process given range xor
# update queries then printing the
# final array
def printFinalArray(arr, N, Q, M):
    # printing initial array
    print("Initial Array: ")
    for i in range(N):
        print(arr[i], end=" ")
    print()

    # Precomputation array
    # used for range update
    prefix = [0] * (N + 1)

    # Traverse the given queries
    for i in range(M):
        # Stores range L, R and U for
        # each query
        L = Q[i][0]
        R = Q[i][1]
        U = Q[i][2]

        for i in range(L, R + 1):
            # Updating L and R + 1 with U
            prefix[L] = prefix[L] ^ U
            prefix[R + 1] = prefix[R + 1] ^ U

    # Taking prefix xor
    # so that every U for M queries
    # carries itself forward from L
    # to R and end at R + 1
    for i in range(1, N):
        prefix[i] = prefix[i] ^ prefix[i - 1]

    # finally printing Final array
    print("Final Array: ")
    for i in range(N):
        # Taking xor with initial array of
        # prefix array so range updates
        # can be made in initial array
        arr[i] = arr[i] ^ prefix[i]
        print(arr[i], end=" ")


# Driver Code
arr = [0, 0, 0, 0, 0, 0, 0]
Q = [[2, 4, 1], [0, 4, 2], [1, 5, 3]]
N = len(arr)
M = len(Q)

# Function Call
printFinalArray(arr, N, Q, M)

# This code is contributed by Pushpesh Raj.
