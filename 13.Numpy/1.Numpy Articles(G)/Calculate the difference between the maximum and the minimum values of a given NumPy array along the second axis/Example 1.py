# import library
import numpy as np

# create a numpy 2d-array
x = np.array([[100, 20, 305],
			[ 200, 40, 300]])

print("given array:\n", x)

# get maximum element row
# wise from numpy array
max1 = np.amax(x ,1)

# get minimum element row
# wise from numpy array
min1 = np.amin(x, 1)

# print the row-wise max
# and min difference
print("difference:\n", max1 - min1)
