# import numpy
import numpy as np
from numpy.polynomial import chebyshev as C

s1 = (4, 6, 8)
s2 = (3, 5, 7)

# using np.chebdiv() method
gfg = C.chebdiv(s1, s2)

print(gfg)
