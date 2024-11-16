# import numpy
import numpy as np
import numpy.polynomial.chebyshev as cheb

# using np.chebgrid3d() method
gfg = cheb.chebgrid3d((2, 5), (1, 3), (5, 6, -3), (2, -4, 1))

print(gfg)
