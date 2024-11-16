# import numpy library
import numpy as np

# create an array
x = np.array([1, 2, 3,
			4, 6, 7,
			8, 9, 10,
			0, 89, 67])

# print array
print(x)

# Test if none of the elements
# of the said array is zero
print(np.all(x))
