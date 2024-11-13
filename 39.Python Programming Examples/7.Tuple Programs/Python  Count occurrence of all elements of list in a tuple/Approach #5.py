# Python3 Program to count occurrence
# of all elements of list in a tuple
import numpy as np


def countOccurrence(tup, lst):
    return np.in1d(tup, lst).sum()


# Driver Code
tup = ('a', 'a', 'c', 'b', 'd')
lst = ['a', 'b']
print(countOccurrence(tup, lst))
