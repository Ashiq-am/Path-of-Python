# Python3 program to Divide list of strings
# into sub lists based on string length
from itertools import groupby


def divideList(lst):
    res = dict((l, list(g)) for l, g in groupby(lst, key=len))

    # Sorting dict by key
    res = sorted(res.items(), key=lambda kv: (kv[0], kv[1]))

    # Removing key from list of tuple
    return [el[1:] for el in (tuple(x) for x in res)]


# Driver code
lst = ['The', 'art', 'of', 'programming']
print(divideList(lst))
