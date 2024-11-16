# import numpy
import numpy as np
import numpy.polynomial.chebyshev as cheb

# using np.chebfromroots() method
gfg = cheb.chebfromroots((-3, 4, -5, 1, 10))

print(gfg)
