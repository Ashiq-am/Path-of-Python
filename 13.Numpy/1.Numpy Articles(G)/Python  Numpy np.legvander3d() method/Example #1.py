# import numpy
import numpy as np
import numpy.polynomial.legendre as geek

# using np.legvander3d() method
ans = geek.legvander3d((1, 3, 5), (2, 4, 6), (1, 2, 3), [2, 2, 2])

print(ans)
