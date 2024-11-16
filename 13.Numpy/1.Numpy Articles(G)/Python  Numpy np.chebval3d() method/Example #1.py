# import numpy
import numpy as np
import numpy.polynomial.chebyshev as cheb

# using np.chebval3d() method
gfg = cheb.chebval3d((2, 5), (1, 3), (4, 8), (2, -4, 1))

print(gfg)
