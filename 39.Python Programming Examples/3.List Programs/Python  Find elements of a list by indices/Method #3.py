# Python3 program to Find elements of a
# list by indices present in another list
from operator import itemgetter


def findElements(lst1, lst2):
    return list((itemgetter(*lst2)(lst1)))


# Driver code
lst1 = [10, 20, 30, 40, 50]
lst2 = [0, 2, 4]
print(findElements(lst1, lst2))
