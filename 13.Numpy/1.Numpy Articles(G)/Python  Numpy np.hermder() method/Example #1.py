# import numpy and harmder
import numpy as np
from numpy.polynomial.hermite import hermder

series = np.array([2, 0.3, 4, 0.5, 6])
# using np.harmder() method
gfg = hermder(series, m = 1)

print(gfg)
