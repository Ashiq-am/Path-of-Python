# Python program explaining
# numpy.legsub() method

# importing numpy as np
# and numpy.polynomial.legendre module as geek
import numpy as np
import numpy.polynomial.legendre as geek

# Legendre series coefficients

s1 = (2, 4, 8)
s2 = (1, 3, 5)

# using np.legsub() method
res = geek.legsub(s1, s2)

# Resulting Legendre series
print(res)
