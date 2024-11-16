# Python code to demonstrate working of
# np.lexsort()
import numpy as np

# Numpy array created
a = np.array([9, 3, 1, 3, 4, 3, 6]) # First column
b = np.array([4, 6, 9, 2, 1, 8, 7]) # Second column
print('column a, column b')
for (i, j) in zip(a, b):
	print(i, ' ', j)

ind = np.lexsort((b, a)) # Sort by a then by b
print('Sorted indices->', ind)
