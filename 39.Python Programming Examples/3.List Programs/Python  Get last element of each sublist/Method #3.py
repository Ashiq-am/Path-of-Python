# Python3 program to extract first and last
# element of each sublist in a list of lists
from operator import itemgetter


def Extract(lst):
    return list(map(itemgetter(-1), lst))


# Driver code
lst = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(Extract(lst))
