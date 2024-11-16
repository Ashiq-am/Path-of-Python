# import numpy
import numpy as np
import numpy.polynomial.chebyshev as cheb

# using np.chebval() method
gfg = cheb.chebval((2, 5), (2, -4, 1))

print(gfg)
