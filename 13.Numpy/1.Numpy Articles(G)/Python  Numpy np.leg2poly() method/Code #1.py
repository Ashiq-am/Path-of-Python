# Python program explaining
# numpy.leg2poly() method

# importing numpy as np
# and numpy.polynomial.legendre module as geek
import numpy as np
import numpy.polynomial.legendre as geek

# Input legendre series coefficients

c = np.array([0.1, 0.2, 0.3, 0.4, 0.5])

# using np.leg2poly() method
res = geek.leg2poly(c)

# Resulting equivalent polynomial series coefficient
print(res)
