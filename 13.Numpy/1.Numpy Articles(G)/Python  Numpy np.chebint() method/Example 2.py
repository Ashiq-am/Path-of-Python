# import numpy
import numpy as np
from numpy.polynomial import chebyshev as C

x = np.array([2, 5, 7, 11])
# using np.chebint() method
gfg = C.chebint(x, 2)

print(gfg)
