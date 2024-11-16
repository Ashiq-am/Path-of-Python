# import numpy
import numpy as np
import numpy.polynomial.chebyshev as cheb

# using np.chebfit() method
gfg = cheb.chebfit((-3, 4, 10), (1, 2, 3), 3)

print(gfg)
