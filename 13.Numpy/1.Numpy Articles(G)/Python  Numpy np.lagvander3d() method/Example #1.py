# import numpy
import numpy as np
import numpy.polynomial.laguerre as geek

# using np.lagvander3d() method
ans = geek.lagvander3d((1, 3, 5), (2, 4, 6), (1, 2, 3), [2, 2, 2])

print(ans)
