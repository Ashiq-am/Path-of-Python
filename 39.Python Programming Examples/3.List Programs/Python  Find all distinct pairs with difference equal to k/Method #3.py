# Python3 program to Find all distinct
# pairs with difference equal to k
from itertools import combinations


def findPairs(lst, k):
    return [(x, y) for x, y in combinations(lst, r=2)
            if abs(x - y) == k]


# Driver code
lst = [1, 5, 3, 4, 2]
k = 3
print(findPairs(lst, k))
