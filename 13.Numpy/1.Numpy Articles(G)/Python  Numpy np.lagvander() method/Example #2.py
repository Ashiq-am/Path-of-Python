# import numpy
import numpy as np
import numpy.polynomial.laguerre as geek

# using np.lagvander() method
gfg = geek.lagvander((2, 5, 1, 12), 5)

print(gfg)
