# importing numpy package for
# creating arrays
import numpy as np

# importing scipy
from scipy import ndimage

a = np.arange(25.).reshape((5, 5))

vals = [[0.3, 1], [0.5, 1]]

# calculating mode
print(ndimage.map_coordinates(a, vals, order=1, mode='nearest'))
print(ndimage.map_coordinates(a, vals, order=1, cval=0, output=bool))
print(ndimage.map_coordinates(a, vals, order=1))
