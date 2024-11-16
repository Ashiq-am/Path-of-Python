import numpy as np

a = np.array([2, 3, 4, 5, 3, 3,
			5, 4, 7, 8, 3])

# Count '3' in numpy array
c = a[a == 3].shape[0]

print('Occurrences of "3" in array is: ', c)
