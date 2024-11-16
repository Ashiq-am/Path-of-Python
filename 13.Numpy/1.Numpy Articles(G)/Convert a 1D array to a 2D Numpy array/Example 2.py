import numpy as np
# 1-D array having elements [1 2 3 4 5 6 7 8]
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Print the 1-D array
print('Before reshaping:')
print(arr)
print('\n')

# let us try to convert into 2-D array having dimension 3x3
arr1 = arr.reshape(3, 3)
print('After reshaping having dimension 3x3:')
print(arr1)
print('\n')
