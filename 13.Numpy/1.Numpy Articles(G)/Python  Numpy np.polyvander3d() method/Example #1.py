# import numpy
import numpy as np
import numpy.polynomial.polynomial as geek

# using np.polyvander3d() method
ans = geek.polyvander3d((1, 3, 5), (2, 4, 6), (1, 2, 3), [2, 2, 2])

print(ans)
