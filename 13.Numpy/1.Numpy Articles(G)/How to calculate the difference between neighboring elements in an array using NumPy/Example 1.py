# import library
import numpy as np

# create a numpy 1d-array
arr = np.array([1, 12, 3, 14, 5,
			16, 7, 18, 9, 110])

# finding the difference between
# neighboring elements
result = np.diff(arr)

print(result)
