# Python program explaining
# numpy.lagder() method

# importing numpy as np
# and numpy.polynomial.laguerre module as geek
import numpy as np
import numpy.polynomial.laguerre as geek

# Laguerre series coefficients
s = (1, 2, 3, 4, 5)

# using np.lagder() method
res = geek.lagder(s, m=2, scl=0.5)

# Resulting laguerre series
print(res)
