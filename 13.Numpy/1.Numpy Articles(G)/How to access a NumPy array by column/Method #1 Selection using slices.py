# Python code to select row and column
# in NumPy

import numpy as np

array = [[1, 13, 6], [9, 4, 7], [19, 16, 2]]

# defining array
arr = np.array(array)

print('printing array as it is')
print(arr)

print('printing 0th row')
print(arr[0, :])

print('printing 2nd column')
print(arr[:, 2])

# multiple columns or rows can be selected as well
print('selecting 0th and 1st row simultaneously')
print(arr[:,[0,1]])
