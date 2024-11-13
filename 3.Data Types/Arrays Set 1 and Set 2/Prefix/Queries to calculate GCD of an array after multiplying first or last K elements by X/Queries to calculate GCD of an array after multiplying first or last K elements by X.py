# Python 3 program for the above approach
from math import gcd


# Function to find the GCD after performing
# each query on array elements
def findGCDQueries(arr, N, Queries, Q):
    # Stores prefix array and suffix
    # array
    prefix = [0 for i in range(N)]
    suffix = [0 for i in range(N)]

    prefix[0] = arr[0]
    suffix[N - 1] = arr[N - 1]

    # Build prefix array
    for i in range(1, N, 1):
        prefix[i] = gcd(prefix[i - 1], arr[i])

    # Build suffix array
    i = N - 2
    while (i >= 0):
        suffix[i] = gcd(suffix[i + 1], arr[i])
        i -= 1

    # Traverse queries array
    for i in range(Q):
        a = Queries[i][0]
        K = Queries[i][1]
        X = Queries[i][2]

        # Edge Case when update is
        # is required till the end
        if (K == N):
            print(prefix[N - 1] * X, end=" ")
            continue

        # Edge Case when update is
        # is required till the front
        if (a == 1):
            print(gcd(prefix[K - 1] * X, suffix[K]), end=" ")

        # Find the resultant operation
        # for each query
        else:
            print(gcd(suffix[N - K] * X, prefix[N - K - 1]), end=" ")


# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 8]
    N = len(arr)
    Queries = [[1, 2, 2], [2, 4, 5]]
    Q = len(Queries)
    findGCDQueries(arr, N, Queries, Q)

# This code is contributed by SURENDRA_GANGWAR.
