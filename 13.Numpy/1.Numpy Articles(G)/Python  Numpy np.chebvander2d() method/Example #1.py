# import numpy
import numpy as np
import numpy.polynomial.chebyshev as cheb

# using np.chebvander2d() method
gfg = cheb.chebvander2d((2, 4, 8, 1), (2, 4, 8, 1), 2)

print(gfg)
