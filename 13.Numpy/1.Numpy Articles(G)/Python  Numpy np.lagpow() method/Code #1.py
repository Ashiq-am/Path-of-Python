# Python program explaining
# numpy.lagpow() method

# importing numpy as np
# and numpy.polynomial.laguerre module as geek
import numpy as np
import numpy.polynomial.laguerre as geek

# Input laguerre series coefficients

s = (2, 4, 8)

# using np.lagpow() method
res = geek.lagpow(s, pow=3)

# Resulting laguerre series coefficient
print(res)
