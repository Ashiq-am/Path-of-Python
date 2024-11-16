# import library
import numpy as np

# create a numpy 2d-array
array = np.array([[1, -2, 3],
				[-4, 5, -6]])

print("Given array:\n",
	array)

# find element-wise
# absolute value
rslt = np.absolute(array)

print("Absolute array:\n",
	rslt)
