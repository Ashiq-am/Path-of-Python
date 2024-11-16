# import numpy and hermetrim
import numpy as np
from numpy.polynomial.hermite_e import hermetrim

series = np.array([1, 0, 0, 0, 0, 0])

# using np.hermetrim() method
gfg = hermetrim(series, tol = 0)

print(gfg)
