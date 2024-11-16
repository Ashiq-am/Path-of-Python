# Python program explaining
# numpy.leg2poly() method

# importing numpy as np
# and numpy.polynomial.legendre module as geek
import numpy as np
import numpy.polynomial.legendre as geek

# Input legendre series coefficients

c = (1, 2, 3, 4, 5)

# using np.leg2poly() method
res = geek.leg2poly(c)

# Resulting equivalent polynomial series coefficient
print(res)
