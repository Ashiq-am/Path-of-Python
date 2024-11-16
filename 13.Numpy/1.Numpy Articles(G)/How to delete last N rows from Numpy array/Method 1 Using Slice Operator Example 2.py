# importing numpy module
import numpy as np

# create an array with 5 rows and
# 4 columns
a = np.array([[21, 7, 8, 9], [34, 10, 11, 12],
			[1, 3, 14, 15], [1, 6, 17, 18],
			[4, 5, 6, 7]])

# use for loop to iterate over the
# elements
for i in range(1, len(a)+1):
	print("Iteration No", i, "deleted", i, "Rows")
	print("Remaining data present in the array is\n ", a[:-i])
