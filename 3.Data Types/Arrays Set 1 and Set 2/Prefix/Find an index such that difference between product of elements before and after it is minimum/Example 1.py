# Python3 implementation of the approach

# Function to return the index i such that
# the absolute difference between product of
# elements up to that index and the product of
# rest of the elements of the array is minimum
def findIndex(a, n):
    # To store the required index
    res, min_diff = None, float('inf')

    # Prefix product array
    prod = [None] * n
    prod[0] = a[0]

    # Compute the product array
    for i in range(1, n):
        prod[i] = prod[i - 1] * a[i]

    # Iterate the product array to find the index
    for i in range(0, n - 1):
        curr_diff = abs((prod[n - 1] // prod[i]) - prod[i])

        if curr_diff < min_diff:
            min_diff = curr_diff
            res = i

    return res


# Driver code
if __name__ == "__main__":
    arr = [3, 2, 5, 7, 2, 9]
    N = len(arr)

    print(findIndex(arr, N))

# This code is contributed by Rituraj Jain
