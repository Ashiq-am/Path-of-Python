# import numpy and hermefromroots
import numpy as np
from numpy.polynomial.hermite_e import hermefromroots

series = np.array([1, 0, 0, 1, 1, 0])
# using np.hermefromroots() method
gfg = hermefromroots(series)

print(gfg)
