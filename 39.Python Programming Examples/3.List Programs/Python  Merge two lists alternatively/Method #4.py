# Python3 program to merge two lists
# alternatively
import numpy as np


def countList(lst1, lst2):
    return np.array([[i, j] for i, j in zip(lst1, lst2)]).ravel()


# Driver code
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
print(countList(lst1, lst2))
