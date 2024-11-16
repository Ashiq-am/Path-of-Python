# import numpy
import numpy as np
from numpy import polynomial as P

x = np.array([2, 3, 5, 7, 11])

# using np.cheb2poly() method
gfg = P.Chebyshev(x)
gfg = gfg.convert(kind = P.Polynomial)
gfg = P.chebyshev.cheb2poly(gfg)

print(gfg)
