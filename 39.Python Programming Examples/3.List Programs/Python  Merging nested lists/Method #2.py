# Python3 program to find Greatest common
# intersection of two nested lists
import itertools
from functools import reduce


def GCI(lst1, lst2):
    temp1 = reduce(list.__add__, lst1)
    temp2 = reduce(list.__add__, lst2)
    lst3 = list(filter(None, [list(set(o1) & set(o2))
                              for o1 in lst1 for o2 in lst2]))

    temp = filter(lambda x: x not in temp1 or x not in temp2,
                  set(temp1) | set(temp2))
    lst3.append(list(temp))

    return lst3


# Driver code
lst1 = [[5, 9], [8, 2, 6], [3, 4]]
lst2 = [[9, 5, 8], [2, 6], [3, 4, 1]]
print(GCI(lst1, lst2))
