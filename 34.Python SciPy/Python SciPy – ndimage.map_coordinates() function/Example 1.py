# importing numpy package for
# creating arrays
import numpy as np

# importing scipy
from scipy import ndimage

# creating an array from 0 to 15 values
a = np.arange(16.).reshape((4, 4))

# finding coordinates
ndimage.map_coordinates(a, [[0.3, 1], [0.5, 1]], order=1)
