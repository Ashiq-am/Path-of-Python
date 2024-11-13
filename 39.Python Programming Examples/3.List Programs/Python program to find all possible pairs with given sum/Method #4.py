# Python3 program to find all pairs in
# a list of integers with given sum
from itertools import combinations


def findPairs(lst, K):
    return [pair for pair in combinations(lst, 2) if sum(pair) == K]


# Driver code
lst = [1, 5, 3, 7, 9]
K = 12
print(findPairs(lst, K))
