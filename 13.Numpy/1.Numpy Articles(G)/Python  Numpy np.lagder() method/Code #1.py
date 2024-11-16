# Python program explaining
# numpy.lagder() method

# importing numpy as np
# and numpy.polynomial.laguerre module as geek
import numpy as np
import numpy.polynomial.laguerre as geek

# Input laguerre series coefficients

s = (2, 4, 8)

# using np.lagder() method
res = geek.lagder(s)

# Resulting laguerre series coefficient
print(res)
