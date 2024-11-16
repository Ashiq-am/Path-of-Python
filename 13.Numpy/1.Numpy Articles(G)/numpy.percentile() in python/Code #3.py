# Python Program illustrating
# numpy.percentile() method

import numpy as np

# 2D array
arr = [[14, 17, 12, 33, 44],
	[15, 6, 27, 8, 19],
	[23, 2, 54, 1, 4,]]
print("\narr : \n", arr)

# Percentile along the axis = 1
print("\n50th Percentile of arr, axis = 1 : ",
	np.percentile(arr, 50, axis =1))
print("0th Percentile of arr, axis = 1 : ",
	np.percentile(arr, 0, axis =1))

print("\n0th Percentile of arr, axis = 1 : \n",
	np.percentile(arr, 50, axis =1, keepdims=True))
print("\n0th Percentile of arr, axis = 1 : \n",
	np.percentile(arr, 0, axis =1, keepdims=True))
