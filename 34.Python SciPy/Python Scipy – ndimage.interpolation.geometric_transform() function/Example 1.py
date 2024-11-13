from scipy import ndimage

# importing numpy module for
# processing the arrays
import numpy as np

# creating an 2 dimensional array with
# 5 * 5 dimensions
a = np.arange(25).reshape((5, 5))

print('a')
print(a)


# reducing dimensions function
def shift_func(output_coords):
    return (output_coords[0] - 0.7, output_coords[1] - 0.7)


# performing geometric transform operation
ndimage.geometric_transform(a, shift_func)
