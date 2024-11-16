# import numpy
import numpy as np
import numpy.polynomial.chebyshev as cheb

# using np.chebgrid2d() method
gfg = cheb.chebgrid2d((2, 5), (1, 3), (2, -4, 1))

print(gfg)
