# import numpy and harmder
import numpy as np
from numpy.polynomial.hermite import hermder

series = np.array([1, 2, 3, 4, 5])
# using np.harmder() method
gfg = hermder(series, m = 2)

print(gfg)
