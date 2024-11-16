# Python code to create a sorted copy using
# sorted()
import numpy as np

# Numpy array created
a = np.array([9, 3, 1, 7, 4, 3, 6])

# unsorted array print
print('Original array:\n', a)
b = sorted(a)

# sorted list returned to b, b type is
# <class 'list'>
print('New array sorted->', b)

# original array no change
print('Original array->', a)
