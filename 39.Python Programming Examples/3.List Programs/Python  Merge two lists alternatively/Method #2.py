# Python3 program to merge two lists
# alternatively
from itertools import cycle


def countList(lst1, lst2):
    iters = [iter(lst1), iter(lst2)]
    return list(iter.__next__() for iter in cycle(iters))


# Driver code
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
print(countList(lst1, lst2))
