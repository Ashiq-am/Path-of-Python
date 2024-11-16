import numpy as np

# Creating a sample numpy array (in 1D)
ary = np.arange(1, 25, 1)

# Converting the 1 Dimensional array to a 2D array
# (to allow explicitly column and row operations)
ary = ary.reshape(5, 5)

# Displaying the Matrix (use print(ary) in IDE)
print(ary)

# This for loop will iterate over all columns of the array one at a time
for col in range(ary.shape[1]):
	print(ary[:, col])
