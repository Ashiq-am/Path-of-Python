# import library
import numpy as np

# create a numpy 2d-array
arr = np.array([[10, 12, 14],
				[25, 35, 45],
				[12, 18, 20]])

# finding the difference between
# neighboring elements along column
result = np.diff(arr, axis = 0)

print(result)
