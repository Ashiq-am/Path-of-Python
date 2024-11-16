# import numpy and hermepow
import numpy as np
from numpy.polynomial.hermite_e import hermepow

series = np.array([1, 2, 3, 4])

# using np.hermepow() method
gfg = hermepow(series, 2)

print(gfg)
