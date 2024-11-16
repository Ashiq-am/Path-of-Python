# import numpy
import numpy as np
import numpy.polynomial.chebyshev as cheb

# using np.chebfromroots() method
gfg = cheb.chebfromroots((2, 4, 8, 1))

print(gfg)
