# libraries
import numpy as np

# Creating an 2D array of 25 elements
ary = np.array([[ 0, 1, 2, 3, 4],
				[ 5, 6, 7, 8, 9],
				[10, 11, 12, 13, 14],
				[15, 16, 17, 18, 19],
				[20, 21, 22, 23, 24]])


# This loop will iterate through each row of the transposed
# array (equivalent of iterating through each column)
for col in ary.T:
	print(col)
