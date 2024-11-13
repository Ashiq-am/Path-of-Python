# Python3 program to unpack
# tuple of lists
from itertools import chain


def unpackTuple(tup):
    res = []
    for i in chain(*tup):
        res.append(i)

    print(res)


# Driver code
tup = (['a', 'apple'], ['b', 'ball'])
unpackTuple(tup)
