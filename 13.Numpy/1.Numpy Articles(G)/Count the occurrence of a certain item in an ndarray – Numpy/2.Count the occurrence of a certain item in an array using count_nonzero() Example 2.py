import numpy as np

a = np.array([[1, 3, 6],
			[1, 3, 4],
			[5, 3, 6],
			[4, 7, 8],
			[3, 6, 1]])

print('Numpy Array:')
print(a)

# Count '3' in numpy array
c = np.count_nonzero(a == 3)
print('Occurences of "3" in array: ', c)
