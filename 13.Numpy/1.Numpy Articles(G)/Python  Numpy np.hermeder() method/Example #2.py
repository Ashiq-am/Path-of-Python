# import numpy and harmeder
import numpy as np
from numpy.polynomial.hermite_e import hermeder

series = np.array([1, 2, 3, 4, 5, 10])

# using np.harmeder() method
gfg = hermeder(series, m = 3)

print(gfg)
