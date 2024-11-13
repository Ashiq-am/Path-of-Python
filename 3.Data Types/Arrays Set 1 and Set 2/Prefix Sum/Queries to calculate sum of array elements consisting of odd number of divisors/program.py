# Python3 program for the above approach
from math import sqrt


# Function to find the sum of elements
# having odd number of divisors in
# index range [L, R] for Q queries
def OddDivisorsSum(n, q, a, Query):
    # Initialize the dp[] array
    DP = [0] * n

    # Traverse the array, arr[]
    for i in range(n):
        x = sqrt(a[i])

        # If a[i] is a perfect square,
        # then update value of DP[i] to a[i]
        if (x * x == a[i]):
            DP[i] = a[i]

    # Find the prefix sum of DP[] array
    for i in range(1, n):
        DP[i] = DP[i - 1] + DP[i]

    # Iterate through all the queries
    for i in range(q):
        l = Query[i][0]
        r = Query[i][1]

        # Find the sum for each query
        if (l == 0):
            print(DP[r], end=" ")
        else:
            print(DP[r] - DP[l - 1], end=" ")


# Driver Code
if __name__ == '__main__':
    arr = [2, 4, 5, 6, 9]
    N = len(arr)
    Q = 3
    Query = [[0, 2], [1, 3], [1, 4]]
    OddDivisorsSum(N, Q, arr, Query)
