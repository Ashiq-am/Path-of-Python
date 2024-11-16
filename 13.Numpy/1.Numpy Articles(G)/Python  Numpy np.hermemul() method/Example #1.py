# import numpy and hermemul
import numpy as np
from numpy.polynomial.hermite_e import hermemul

series1 = np.array([1, 2, 3, 4])
series2 = np.array([10, 11, 12, 13])

# using np.hermemul() method
gfg = hermemul(series1, series2)

print(gfg)
