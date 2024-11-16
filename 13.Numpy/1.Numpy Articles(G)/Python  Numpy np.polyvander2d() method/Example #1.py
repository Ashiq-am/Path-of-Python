# import numpy
import numpy as np
import numpy.polynomial.polynomial as geek

# using np.polyvander() method
ans = geek.polyvander2d((1, 3, 5, 7), (2, 4, 6, 8), [2, 2])

print(ans)
