# import numpy
import numpy as np
from numpy.polynomial import chebyshev as C

s1 = (4, 6, 8)

# using np.chebmulx() method
gfg = C.chebmulx(s1)

print(gfg)
