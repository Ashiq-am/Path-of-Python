# import numpy and hermfromroot
import numpy as np
from numpy.polynomial.hermite import hermfromroots

roots = np.array([0.1, 2, 0.3, 4])
# using np.hermfromroots() method
gfg = hermfromroots(roots)

print(gfg)
