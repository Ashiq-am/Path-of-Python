# Java implementation of
# simple approach to
# find maximum value after
# m range increments.
import sys


def findMax(n, m, a, b, k):
    arr = [0 for i in range(n + 1)]

    for i in range(m):
        lowerbound = a[i]
        upperbound = b[i]

        arr[lowerbound] += k[i]
        arr[upperbound + 1] -= k[i]

    sum = 0
    res = -1 - sys.maxsize

    for i in range(n):
        sum += arr[i]
        res = max(res, sum)
    return res


n = 5
a = [0, 1, 2]
b = [1, 4, 3]
k = [100, 100, 100]

m = len(a)

print("Maximum value after", "'m' operations is", findMax(n, m, a, b, k))

# This code is contributed by rag2127
