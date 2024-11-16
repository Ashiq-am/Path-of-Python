# import numpy
import numpy as np
import numpy.polynomial.polynomial as geek

# using np.polyvander() method
ans = geek.polyvander((1, 3, 5, 7), 2)

print(ans)
