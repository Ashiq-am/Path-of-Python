# import numpy and hermeval
import numpy as np
from numpy.polynomial.hermite_e import hermeval

series = np.array([1, 2, 3, 4])

# using np.hermeval() method
gfg = hermeval(2, series)

print(gfg)
