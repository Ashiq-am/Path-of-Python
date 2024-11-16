# import numpy
import numpy as np
from numpy.polynomial import chebyshev as C

s1 = (3, 5, 7, 2, 4, 6)

# using np.chebpow() method
gfg = C.chebpow(s1, 2)

print(gfg)
