# Python3 Program to Create list
# with integers within given range
import numpy as np


def createList(r1, r2):
    return np.arange(r1, r2 + 1, 1)


# Driver Code
r1, r2 = -1, 1
print(createList(r1, r2))
