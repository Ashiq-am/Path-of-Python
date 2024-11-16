# Python program explaining
# numpy.lag2poly() method

# importing numpy as np
# and numpy.polynomial.laguerre module as geek
import numpy as np
import numpy.polynomial.laguerre as geek

# Input laguerre series coefficients

c = (1, 2, 3, 4, 5)

# using np.lag2poly() method
res = geek.lag2poly(c)

# Resulting equivalent polynomial series coefficient
print(res)
