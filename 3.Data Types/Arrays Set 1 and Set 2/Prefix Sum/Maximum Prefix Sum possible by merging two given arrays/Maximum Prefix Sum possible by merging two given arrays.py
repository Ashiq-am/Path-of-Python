# Python3 implementation of the
# above approach

def maxPresum(a, b):
    # Stores the maximum prefix
    # sum of the array A[]
    X = max(a[0], 0)

    # Traverse the array A[]
    for i in range(1, len(a)):
        a[i] += a[i - 1]
        X = max(X, a[i])

    # Stores the maximum prefix
    # sum of the array B[]
    Y = max(b[0], 0)

    # Traverse the array B[]
    for i in range(1, len(b)):
        b[i] += b[i - 1]
        Y = max(Y, b[i])

    return X + Y


# Driver code

A = [2, -1, 4, -5]
B = [4, -3, 12, 4, -3]
print(maxPresum(A, B))

# This code is contributed by code_hunt.
