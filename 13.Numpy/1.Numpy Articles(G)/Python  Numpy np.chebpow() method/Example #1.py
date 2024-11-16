# import numpy
import numpy as np
from numpy.polynomial import chebyshev as C

s1 = (4, 6, 8)

# using np.chebpow() method
gfg = C.chebpow(s1, 5)

print(gfg)
