# import numpy
import numpy as np
import numpy.polynomial.chebyshev as cheb

# using np.chebgrid3d() method
gfg = cheb.chebgrid3d((1, -3, 7), (-2, 4, -8), (3, -4, 1), (2, -4, 1, 5, 1))

print(gfg)
