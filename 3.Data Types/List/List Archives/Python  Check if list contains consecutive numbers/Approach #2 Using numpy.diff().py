# Python3 Program to Create list
# with integers within given range
import numpy as np


def checkConsecutive(l):
    n = len(l) - 1
    return (sum(np.diff(sorted(l)) == 1) >= n)


# Driver Code
lst = [2, 3, 1, 4, 5]
print(checkConsecutive(lst))
