# Python program explaining
# numpy.lagsub() method

# importing numpy as np
# and numpy.polynomial.laguerre module as geek
import numpy as np
import numpy.polynomial.laguerre as geek

# Laguerre series coefficients

s1 = (2, 4, 8)
s2 = (1, 3, 5)

# using np.lagsub() method
res = geek.lagsub(s1, s2)

# Resulting laguerre series
print(res)
