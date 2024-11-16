# import numpy
import numpy as np
from numpy.polynomial import chebyshev as C

x = np.array([1, 2, 3])
# using np.chebder() method
gfg = C.chebder(x, 2)

print(gfg)
