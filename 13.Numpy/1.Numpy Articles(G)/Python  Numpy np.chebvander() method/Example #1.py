# import numpy
import numpy as np
import numpy.polynomial.chebyshev as cheb

# using np.chebvander() method
gfg = cheb.chebvander((2, 4, 8, 1), 2)

print(gfg)
