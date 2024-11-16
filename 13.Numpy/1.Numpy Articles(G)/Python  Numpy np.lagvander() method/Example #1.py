# import numpy
import numpy as np
import numpy.polynomial.laguerre as geek

# using np.lagvander() method
gfg = geek.lagvander((1, 3, 5, 7), 2)

print(gfg)
