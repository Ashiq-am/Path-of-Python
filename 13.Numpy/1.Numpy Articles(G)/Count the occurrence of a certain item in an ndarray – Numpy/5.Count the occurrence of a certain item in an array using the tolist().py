import numpy as np

a = np.array([2, 3, 4, 5, 3, 3,
			5, 4, 7, 8, 3])

# Count element '3' in numpy array
c = a.tolist().count(5)
print('Occurences of "3" in array: ', c)
