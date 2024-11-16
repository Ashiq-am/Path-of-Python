# import numpy and hermeval2d
import numpy as np
from numpy.polynomial.hermite_e import hermeval2d

series = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# using np.hermeval2d() method
gfg = hermeval2d(3, 4, series)

print(gfg)
