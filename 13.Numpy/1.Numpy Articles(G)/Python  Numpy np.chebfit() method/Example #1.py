# import numpy
import numpy as np
import numpy.polynomial.chebyshev as cheb

# using np.chebfit() method
gfg = cheb.chebfit((4, -5), (5, 7), 1)

print(gfg)
