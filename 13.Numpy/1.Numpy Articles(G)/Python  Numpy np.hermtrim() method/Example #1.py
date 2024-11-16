# import numpy and hermtrim
import numpy as np
from numpy.polynomial.hermite import hermtrim

series = np.array([2, 0, 4, 0, 6, 1, 1, 1])

# using np.hermtrim() method
gfg = hermtrim(series, tol = 1)

print(gfg)
