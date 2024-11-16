import numpy as np
# 1-D array having elements [1 2 3 4 5 6 7 8]
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Print the 1-D array
print('Before reshaping:')
print(arr)
print('\n')


arr1 = arr.reshape(2, 2, -1)
print('After reshaping:')
print(arr1)
print('\n')
