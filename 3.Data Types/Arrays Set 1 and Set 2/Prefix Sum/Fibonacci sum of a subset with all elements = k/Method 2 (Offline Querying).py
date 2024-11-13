# Python3 program to find fibonacci sum of
# subarray where all elements <= k

from bisect import bisect


# Helper function that multiplies 2 matrices
# F and M of size 2*2, and puts the multiplication
# result back to F


def multiply(F, M):
    x = F[0][0] * M[0][0] + F[0][1] * M[1][0]
    y = F[0][0] * M[0][1] + F[0][1] * M[1][1]
    z = F[1][0] * M[0][0] + F[1][1] * M[1][0]
    w = F[1][0] * M[0][1] + F[1][1] * M[1][1]

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


# Helper function that calculates F
# raise to the power n and puts the
# result in F


def power(F, n):
    M = [[1, 1], [1, 0]]

    # n - 1 times multiply the
    # matrix to [[1, 0], [0, 1]]
    for i in range(1, n):
        multiply(F, M)


# Returns the nth fibonacci number


def fib(n):
    F = [[1, 1], [1, 0]]
    if (n == 0):
        return 0
    power(F, n - 1)

    return F[0][0]


# Return the answer for each query
def processQuery(arr, queries, n, q):
    # build offline queries where each query
    # is of type tuple which stores
    # both K and original Index of the query
    # in the queries array

    offlineQueries = [None] * q

    # Allocate memory to store ans of each query
    ans = [0] * q

    for i in range(q):
        original_index = i
        K = queries[i]
        offlineQueries[i] = (K, original_index)

    # sort offlineQueries
    offlineQueries.sort()

    # i is pointing to the current position
    # array arr fibonacciSum store the
    # fibonacciSum till ith index
    i, fibonacciSum = 0, 0

    for j in range(q):
        currK = offlineQueries[j][0]
        currQueryIndex = offlineQueries[j][1]

        # keep inserting elements to subset
        # while elements are less than
        # current query's K value
        while (i < n and arr[i] <= currK):
            fibonacciSum += fib(arr[i])
            i += 1

        # store the current value of
        # fibonacci sum in the array ans
        # which stores results for the
        # queries in the original order
        ans[currQueryIndex] = fibonacciSum

    return ans


# Driver Code
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 2, 7]
    n = len(arr)

    # sort the array arr
    arr.sort()

    # query array stores q queries
    queries = [2, 10, 6]
    q = len(queries)

    # res stores the result of each query
    res = processQuery(arr, queries, n, q)

    for i in range(q):
        ans = res[i]
        print("Query {} : {}".format(i + 1, ans))
