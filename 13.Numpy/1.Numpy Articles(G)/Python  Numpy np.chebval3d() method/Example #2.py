# import numpy
import numpy as np
import numpy.polynomial.chebyshev as cheb

# using np.chebval3d() method
gfg = cheb.chebval3d((1, 3, 5, 7), (2, 4, 8), (-10, -12), (2, -4, 1, 5, 1))

print(gfg)
