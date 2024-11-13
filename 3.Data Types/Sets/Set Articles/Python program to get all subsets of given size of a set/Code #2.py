# Python Program to Print
# all subsets of given size of a set

import itertools
from itertools import combinations, chain


def findsubsets(s, n):
    return list(map(set, itertools.combinations(s, n)))


# Driver Code
s = {1, 2, 3}
n = 2

print(findsubsets(s, n))
