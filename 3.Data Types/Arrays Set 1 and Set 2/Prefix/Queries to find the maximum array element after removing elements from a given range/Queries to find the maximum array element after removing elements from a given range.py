# Python3 program for the above approach

# Function to find the maximum element
# after removing elements in range [l, r]
def findMaximum(arr, N, Q, queries):
    # Store prefix maximum element
    prefix_max = [0] * (N + 1)

    # Store suffix maximum element
    suffix_max = [0] * (N + 1)

    # Prefix max till first index
    # is first index itself
    prefix_max[0] = arr[0]

    # Traverse the array to fill
    # prefix max array
    for i in range(1, N):
        # Store maximum till index i
        prefix_max[i] = max(prefix_max[i - 1], arr[i])

    # Suffix max till last index
    # is last index itself
    suffix_max[N - 1] = arr[N - 1]

    # Traverse the array to fill
    # suffix max array
    for i in range(N - 2, -1, -1):
        # Store maximum till index i
        suffix_max[i] = max(suffix_max[i + 1], arr[i])

    # Traverse all queries
    for i in range(Q):

        # Store the starting and the
        # ending index of the query
        l = queries[i][0]
        r = queries[i][1]

        # Edge Cases
        if (l == 0 and r == (N - 1)):
            print("0")
        elif (l == 0):
            print(suffix_max[r + 1])
        elif (r == (N - 1)):
            print(prefix_max[l - 1])

        # Otherwise
        else:
            print(max(prefix_max[l - 1], suffix_max[r + 1]))


# Driver Code
if __name__ == '__main__':
    arr = [5, 6, 8, 10, 15]
    N = len(arr)
    queries = [[0, 1], [0, 2], [1, 4]]
    Q = len(queries)
    findMaximum(arr, N, Q, queries)

# This code is contributed by mohit kumar 29.
