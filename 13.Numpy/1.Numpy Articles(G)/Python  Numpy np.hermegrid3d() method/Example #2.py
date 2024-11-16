# import numpy and hermegrid3d
import numpy as np
from numpy.polynomial.hermite_e import hermegrid3d

series = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# using np.hermegrid3d() method
gfg = hermegrid3d([0, 1], [2, 3], [4, 5], series)

print(gfg)
