# import numpy and hermeroots
import numpy as np
from numpy.polynomial.hermite_e import hermeroots

series = np.array([1, 2, 3, 4, 5])
# using np.hermeroots() method
gfg = hermeroots(series)

print(gfg)
