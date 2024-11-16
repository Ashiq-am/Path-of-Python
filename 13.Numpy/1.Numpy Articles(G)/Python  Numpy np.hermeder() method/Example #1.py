# import numpy and harmeder
import numpy as np
from numpy.polynomial.hermite_e import hermeder

series = np.array([2, 0.3, 4, 0.5, 6])

# using np.harmeder() method
gfg = hermeder(series, m = 2)

print(gfg)
