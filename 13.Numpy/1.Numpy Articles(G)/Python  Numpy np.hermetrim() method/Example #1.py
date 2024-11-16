# import numpy and herm1trim
import numpy as np
from numpy.polynomial.hermite_e import hermetrim

series = np.array([2, 0, 4, 0, 6, 1, 1, 1])

# using np.hermetrim() method
gfg = hermetrim(series, tol = 1)

print(gfg)
