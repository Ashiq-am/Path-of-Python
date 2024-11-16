# Python program explaining
# numpy.lagub() method

# importing numpy as np
# and numpy.polynomial.laguerre module as geek
import numpy as np
import numpy.polynomial.laguerre as geek

# Laguerre series coefficients
s1 = (10, 20, 30, 40, 50)
s2 = (2, 4, 6, 8, 10)

# using np.lagsub() method
res = geek.lagsub(s1, s2)

# Resulting laguerre series
print(res)
