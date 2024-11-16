# import library
import numpy as np

# create a 1d-array
x = np.arange(10)

print("Original array:",
	x)

# apply true division
# on each array element
rslt = np.true_divide(x, 3)

print("After the element-wise division:",
	rslt)
