# Python program explaining
# numpy.legmul() method

# importing numpy as np
# and numpy.polynomial.legendre module as geek
import numpy as np
import numpy.polynomial.legendre as geek

# Legendre series coefficients
s1 = (10, 20, 30, 40, 50)
s2 = (2, 4, 6, 8, 10)

# using np.legmul() method
res = geek.legmul(s1, s2)

# Resulting Legendre series
print(res)
