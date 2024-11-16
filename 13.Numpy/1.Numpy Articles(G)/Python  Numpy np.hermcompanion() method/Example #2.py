# import numpy and hermcompanion
import numpy as np
from numpy.polynomial.hermite import hermcompanion

series = np.array([1, 2, 3, 4, 5])
# using np.hermcompanion() method
gfg = hermcompanion(series)

print(gfg)
