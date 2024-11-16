# import numpy and hermefromroots
import numpy as np
from numpy.polynomial.hermite_e import hermefromroots

series = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
# using np.hermefromroots() method
gfg = hermefromroots(series)

print(gfg)
