# Python3 program to increment 1's in
# list based on pattern
from itertools import *


def transform(lst):
    c = count(1)
    return list(chain(*[list(g) if k != 1 else [next(c)] * len(list(g))
                        for k, g in groupby(lst)]))


# Driver code
lst = [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1]
print(transform(lst))
