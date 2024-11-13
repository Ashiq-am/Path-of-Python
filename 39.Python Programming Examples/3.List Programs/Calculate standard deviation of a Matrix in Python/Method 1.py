# import required packages
import numpy as np

# Create matrix
matrix = np.array([[33, 55, 66, 74], [23, 45, 65, 27],
				[87, 96, 34, 54]])

print("Your matrix:\n", matrix)

# use std() method
sd = np.std(matrix)
print("Standard Deviation :\n", sd)
