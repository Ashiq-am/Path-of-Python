# program to select row and column
# in numpy using ellipsis

import numpy as np

# defining array
array = [[1, 13, 6], [9, 4, 7], [19, 16, 2]]

# converting to numpy array
arr = np.array(array)

print('printing array as it is')
print(arr)

print('selecting 0th column')
print(arr[..., 0])

print('selecting 1st row')
print(arr[1, ...])
