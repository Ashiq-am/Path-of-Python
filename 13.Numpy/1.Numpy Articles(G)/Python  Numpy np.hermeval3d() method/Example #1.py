# import numpy and hermeval3d
import numpy as np
from numpy.polynomial.hermite_e import hermeval3d

series = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# using np.hermeval3d() method
gfg = hermeval3d(3, 4, 6, series)

print(gfg)
