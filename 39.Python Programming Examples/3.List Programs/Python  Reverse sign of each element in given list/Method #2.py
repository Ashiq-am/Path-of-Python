# Python3 program to Convert positive
# list integers to negative and vice-versa
import numpy as np


def Convert(lst):
    lst = np.array(lst)
    return list(-lst)


# Driver code
lst = [-1, 2, 3, -4, 5, -6, -7]
print(Convert(lst))
