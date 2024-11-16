# import numpy
import numpy as np
import numpy.polynomial.chebyshev as cheb

# using np.chebval2d() method
gfg = cheb.chebval2d((2, 5), (1, 3), (2, -4, 1))

print(gfg)
