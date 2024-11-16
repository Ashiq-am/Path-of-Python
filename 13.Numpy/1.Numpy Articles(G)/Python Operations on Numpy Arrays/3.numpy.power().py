# Python code to perform power operation
# on NumPy array


import numpy as np


arr = np.array([5, 10, 15])

print('First array is:')
print(arr)

print('\nApplying power function:')
print(np.power(arr, 2))

print('\nSecond array is:')
arr1 = np.array([1, 2, 3])
print(arr1)

print('\nApplying power function again:')
print(np.power(arr, arr1))
