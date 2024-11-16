# importing numpy module
import numpy as np

# create an array with 5 rows and
# 4 columns
a = np.array([[21, 7, 8, 9], [34, 10, 11, 12],
			[1, 3, 14, 15], [1, 6, 17, 18],
			[4, 5, 6, 7]])

# delete last three rows
# using numpy.delete
a = np.delete(a, [2, 3, 4], 0)
print(a)
