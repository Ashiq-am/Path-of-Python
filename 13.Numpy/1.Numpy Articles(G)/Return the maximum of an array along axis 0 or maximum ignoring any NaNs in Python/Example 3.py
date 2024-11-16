# import required packages
import numpy as np

# creating a numpy array with few Nan values
arr = np.array([[1, 0, 3], [10, np.nan, 30],
				[np.nan, 10, 20]])

# display the input array
print("Input array\n", arr)

# return the maximum value in an array
# by ignoring NaNs
print("Max value in array-", np.nanmax(arr))
