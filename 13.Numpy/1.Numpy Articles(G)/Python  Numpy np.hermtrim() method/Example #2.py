# import numpy and hermtrim
import numpy as np
from numpy.polynomial.hermite import hermtrim

series = np.array([1, 0, 0, 0, 0, 0])

# using np.hermtrim() method
gfg = hermtrim(series, tol = 0)

print(gfg)
