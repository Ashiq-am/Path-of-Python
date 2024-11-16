# Python program explaining
# numpy.lagroots() method

# importing numpy as np
# and numpy.polynomial.laguerre module as geek
import numpy as np
import numpy.polynomial.laguerre as geek

# Input laguerre series coefficients

s = (2, 4, 8)

# using np.lagroots() method
res = geek.lagroots(s)

# Resulting laguerre series coefficient
print(res)
