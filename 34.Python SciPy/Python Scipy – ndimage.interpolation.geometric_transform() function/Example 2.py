from scipy import ndimage

# importing numpy module for
# processing the arrays
import numpy as np


# create 4 * 4 dim array.
b = np.arange(16).reshape((4, 4))

# reducing dimensions function
def shift_func(output_coords):

	return (output_coords[0] - 0.1, output_coords[1] - 0.2)


ndimage.geometric_transform(b, shift_func)
