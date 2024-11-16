# import numpy and hermcompanion
import numpy as np
from numpy.polynomial.hermite import hermcompanion

series = np.array([6, 7, 8, 9, 10])
# using np.hermcompanion() method
gfg = hermcompanion(series)

print(gfg)
