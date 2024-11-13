# Python program for the above approach

# Function to find the minimum number
# of increments/decrements of array
# elements by 1 to make signs of
# prefix sum array elements alternating
def minimumOperations(A, N):
    # Case 1. neg - pos - neg
    cur_prefix_1 = 0

    # Stores the current sign of
    # the prefix sum of array
    parity = -1

    # Stores minimum number of operations
    # for Case 1
    minOperationsCase1 = 0

    # Traverse the array
    for i in range(N):

        cur_prefix_1 += A[i]

        # Checking both conditions
        if (cur_prefix_1 == 0
                or parity * cur_prefix_1 < 0):
            minOperationsCase1 += abs(parity - cur_prefix_1)

            # Update the current prefix1 to
            # currentPrefixSum
            cur_prefix_1 = parity

        parity *= -1

    # Case 2. pos - neg - pos
    cur_prefix_2 = 0

    # Stores the prefix sum of array
    parity = 1

    # Stores minimum number of operations
    # for Case 1
    minOperationsCase2 = 0

    for i in range(N):

        cur_prefix_2 += A[i]

        # Checking both conditions
        if (cur_prefix_2 == 0
                or parity * cur_prefix_2 < 0):
            minOperationsCase2 += abs(parity - cur_prefix_2)

            # Update the current prefix2 to
            # currentPrefixSum
            cur_prefix_2 = parity

        parity *= -1

    return min(minOperationsCase1,
               minOperationsCase2)


# Driver Code

A = [1, -3, 1, 0]
N = len(A)
print(minimumOperations(A, N))

# This code is contributed by splevel62.
