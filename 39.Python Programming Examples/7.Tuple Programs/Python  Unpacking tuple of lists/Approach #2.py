# Python3 program to unpack
# tuple of lists
from functools import reduce
import numpy


def unpackTuple(tup):
    print(reduce(numpy.append, tup))


# Driver code
tup = (['a', 'apple'], ['b', 'ball'])
unpackTuple(tup)
