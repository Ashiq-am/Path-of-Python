# Python3 program to Merge first and last
# elements separately in a list of lists
import numpy as np


def merge(lst):
    arr = np.array(lst)
    return arr.T.tolist()


# Driver code
lst = [['x', 'y'], ['a', 'b'], ['m', 'n']]
print(merge(lst))
