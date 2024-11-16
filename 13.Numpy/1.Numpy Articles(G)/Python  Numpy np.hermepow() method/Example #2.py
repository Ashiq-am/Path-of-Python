# import numpy and hermepow
import numpy as np
from numpy.polynomial.hermite_e import hermepow

series = np.array([11, 22, 33, 44])

# using np.hermepow() method
gfg = hermepow(series, 3)

print(gfg)
