# import numpy and hermemulx
import numpy as np
from numpy.polynomial.hermite_e import hermemulx

series = np.array([1, 2, 3, 4])

# using np.hermemulx() method
gfg = hermemulx(series)

print(gfg)
