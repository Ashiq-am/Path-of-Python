# import numpy
import numpy as np
import numpy.polynomial.chebyshev as cheb

# using np.chebgrid2d() method
gfg = cheb.chebgrid2d((1, 3, 5, 7), (2, 4, 8), (2, -4, 1, 5, 1))

print(gfg)
