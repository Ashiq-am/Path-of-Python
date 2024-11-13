# Python3 program to merge two lists
# alternatively
import operator
from functools import reduce


def countList(lst1, lst2):
    return reduce(operator.add, zip(lst1, lst2))


# Driver code
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
print(countList(lst1, lst2))
