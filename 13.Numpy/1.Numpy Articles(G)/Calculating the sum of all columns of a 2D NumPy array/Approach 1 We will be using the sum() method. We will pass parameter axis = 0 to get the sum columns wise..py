# importing numpy
import numpy as np

# initialize the 2-d array
arr = np.array([[1, 2, 3, 4, 5],
				[5, 6, 7, 8, 9],
				[2, 1, 5, 7, 8],
				[2, 9, 3, 1, 0]])

# calculating column wise sum
sum_2d = arr.sum(axis = 0)

# displaying the sum
print("Column wise sum is :\n", sum_2d)
