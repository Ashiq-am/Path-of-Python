# Python3 program for the above approach
import math


# Function count the number of elements
# having odd number of divisors
def OddDivisorsCount(n, q, a, Query):
    # Initialise dp[] array
    DP = [0 for i in range(n)]

    # Precomputation
    for i in range(n):
        x = int(math.sqrt(a[i]))

        if (x * x == a[i]):
            DP[i] = 1

    # Find the Prefix Sum
    for i in range(1, n):
        DP[i] = DP[i - 1] + DP[i]

    l = 0
    r = 0

    # Iterate for each query
    for i in range(q):
        l = Query[i][0]
        r = Query[i][1]

        # Find the answer for each query
        if (l == 0):
            print(DP[r])
        else:
            print(DP[r] - DP[l - 1])


# Driver code
if __name__ == "__main__":
    N = 5
    Q = 3

    # Given array arr[]
    arr = [2, 4, 5, 6, 9]

    # Given Query
    Query = [[0, 2],
             [1, 3],
             [1, 4]]

    # Function call
    OddDivisorsCount(N, Q, arr, Query)


