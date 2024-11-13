# Python3 program to find all pairs in
# a list of integers with given sum
from collections import Counter


def findPairs(lst, K):
    res = []
    count = Counter(lst)

    for x in lst:
        y = K - x
        if (x != y and count[y]) or (x == y and count[y] > 1):
            res.append((x, y))
            count.subtract((x, y))

    return res


# Driver code
lst = [1, 5, 3, 7, 9]
K = 12
print(findPairs(lst, K))
