# Python program explaining
# numpy.lagroot() method

# importing numpy as np
# and numpy.polynomial.laguerre module as geek
import numpy as np
import numpy.polynomial.laguerre as geek

# Laguerre series coefficients
s = (1, 2, 3, 4, 5)

# using np.lagroots() method
res = geek.lagroots(s)

# Resulting laguerre series
print(res)
