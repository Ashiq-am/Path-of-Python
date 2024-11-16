# import numpy and hermemulx
import numpy as np
from numpy.polynomial.hermite_e import hermemulx

series = np.array([11, 22, 33, 44])

# using np.hermemulx() method
gfg = hermemulx(series)

print(gfg)
