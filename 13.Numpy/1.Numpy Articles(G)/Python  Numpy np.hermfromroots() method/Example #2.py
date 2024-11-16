# import numpy and hermfromroot
import numpy as np
from numpy.polynomial.hermite import hermfromroots

roots = np.array([1, 2, 3, 4, 1.0001])
# using np.hermfromroots() method
gfg = hermfromroots(roots)

print(gfg)
