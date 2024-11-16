# import numpy
import numpy as np
from numpy.polynomial import chebyshev as C

s1 = (4, 6, 8, 1, 3, 5)
s2 = (3, 5, 7, 2, 4, 6)
# using np.chebadd() method
gfg = C.chebadd(s1, s2)

print(gfg)
