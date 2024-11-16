# import numpy and hermegrid2d
import numpy as np
from numpy.polynomial.hermite_e import hermegrid2d

series = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# using np.hermegrid2d() method
gfg = hermegrid2d(3, 4, series)

print(gfg)
