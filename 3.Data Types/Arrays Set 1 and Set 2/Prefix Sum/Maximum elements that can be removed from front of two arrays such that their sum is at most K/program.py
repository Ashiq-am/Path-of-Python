# Python3 program for the above approach

# Function to find the maximum number
# of items that can be removed from
# both the arrays
def maxItems(n, m, a, b, K):
    # Stores the maximum item count
    count = 0

    # Stores the prefix sum of the
    # cost of items
    A = [0 for i in range(n + 1)]
    B = [0 for i in range(m + 1)]

    # Build the prefix sum for
    # the array A[]
    for i in range(1, n + 1, 1):
        # Update the value of A[i]
        A[i] = a[i - 1] + A[i - 1]

    # Build the prefix sum for
    # the array B[]
    for i in range(1, m + 1, 1):
        # Update the value of B[i]
        B[i] = b[i - 1] + B[i - 1]

    # Iterate through each item
    # of the array A[]
    for i in range(n + 1):

        # If A[i] exceeds K
        if (A[i] > K):
            break

        # Store the remaining amount
        # after taking top i elements
        # from the array A
        rem = K - A[i]

        # Store the number of items
        # possible to take from the
        # array B[]
        j = 0

        # Store low and high bounds
        # for binary search
        lo = 0
        hi = m

        # Binary search to find
        # number of item that
        # can be taken from stack
        # B in rem amount
        while (lo <= hi):

            # Calculate the mid value
            mid = (lo + hi) // 2

            if (B[mid] <= rem):

                # Update the value
                # of j and lo
                j = mid
                lo = mid + 1

            else:

                # Update the value
                # of the hi
                hi = mid - 1

        # Store the maximum of total
        # item count
        count = max(j + i, count)

    # Print the result
    print(count)


# Driver Code
if __name__ == '__main__':
    n = 4
    m = 5
    K = 7
    A = [2, 4, 7, 3]
    B = [1, 9, 3, 4, 5]

    maxItems(n, m, A, B, K)
