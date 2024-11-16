# import numpy
import numpy as np
import numpy.polynomial.chebyshev as cheb

# using np.chebvander() method
gfg = cheb.chebvander((3, 5, 1, 10), 4)

print(gfg)
