# Python3 program to find most common
# element in each column in a 2D list
from scipy.stats import mode
import numpy as np


def mostCommon(lst):
    val, count = mode(lst, axis=0)
    return val.ravel().tolist()


# Driver code
lst = [[1, 1, 3],
       [2, 3, 3],
       [3, 2, 2],
       [2, 1, 3]]
print(mostCommon(lst))
