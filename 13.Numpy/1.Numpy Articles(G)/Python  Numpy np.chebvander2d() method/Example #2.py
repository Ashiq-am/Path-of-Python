# import numpy
import numpy as np
import numpy.polynomial.chebyshev as cheb

# using np.chebvander2d() method
gfg = cheb.chebvander2d((3, 5, 1, 10), (3, 5, 1, 10), 4)

print(gfg)
