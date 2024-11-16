# import numpy
import numpy as np
import numpy.polynomial.chebyshev as cheb

# using np.chebval() method
gfg = cheb.chebval((1, 3, 5, 7), (2, -4, 1, 5, 1))

print(gfg)
