# Python program explaining
# numpy.lagdiv() method

# importing numpy as np
# and numpy.polynomial.laguerre module as geek
import numpy as np
import numpy.polynomial.laguerre as geek

# Laguerre series coefficients
s1 = (10, 20, 30, 40, 50)
s2 = (2, 4, 6, 8, 10)

# using np.lagdiv() method
res = geek.lagdiv(s1, s2)

# Resulting laguerre series
print(res)
