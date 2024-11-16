# import numpy and hermeroots
import numpy as np
from numpy.polynomial.hermite_e import hermeroots

series = np.array([1, 0, 0, 1, 1, 0])
# using np.hermeroots() method
gfg = hermeroots(series)

print(gfg)
