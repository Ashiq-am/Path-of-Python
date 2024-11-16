# import numpy
import numpy as np
import numpy.polynomial.laguerre as geek

# using np.lagvander() method
ans = geek.lagvander2d((1, 3, 5, 7), (2, 4, 6, 8), [2, 2])

print(ans)
