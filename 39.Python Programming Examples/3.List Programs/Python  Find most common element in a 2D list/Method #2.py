# Python3 program to find most
# common element in a 2D list
from itertools import chain
from collections import Counter


def mostCommon(lst):
    flatList = chain.from_iterable(lst)
    return Counter(flatList).most_common(1)[0][0]


# Driver code
lst = [[10, 20, 30], [20, 50, 10], [30, 50, 10]]
print(mostCommon(lst))
