import numpy as np

a = np.array([2, 3, 4, 5, 3, 3, 5, 4, 7, 8, 3])

print('Numpy Array:')
print(a)

# Count element '3' in numpy array
c = np.count_nonzero(a == 3)
print('Total occurences of "3" in array: ', c)
