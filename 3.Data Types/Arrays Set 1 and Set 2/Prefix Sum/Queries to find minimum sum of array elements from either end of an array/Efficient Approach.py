# Python3 implementation
# of the above approach

# Function to find the minimum sum
# for the given queries
def calculateQuery(arr, N, query, M):
    # Stores prefix and suffix sums
    prefix = 0
    suffix = 0

    # Stores pairs of prefix and suffix sums
    mp = {}

    # Traverse the array
    for i in range(N):
        # Add element to prefix
        prefix += arr[i]

        # Store prefix for each element
        mp[arr[i]] = [prefix, 0]

    # Traverse the array in reverse
    for i in range(N - 1, -1, -1):
        # Add element to suffix
        suffix += arr[i]

        # Storing suffix for each element
        mp[arr[i]] = [mp[arr[i]][0], suffix]

    # Traverse the array queries[]
    for i in range(M):
        X = query[i]

        # Minimum of suffix
        # and prefix sums
        print(min(mp[X][0], mp[X][1]), end=" ")


# Driver Code
arr = [2, 3, 6, 7, 4, 5, 30]
queries = [6, 5]
N = len(arr)
M = len(queries)

calculateQuery(arr, N, queries, M)

# This code is contributed by avanitrachhadiya2155
