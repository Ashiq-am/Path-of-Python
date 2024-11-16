# Python program explaining
# numpy.legint() method

# importing numpy as np
# and numpy.polynomial.legendre module as geek
import numpy as np
import numpy.polynomial.legendre as geek

# Legendre series coefficients

s1 = (2, 4, 8)

# using np.legint() method
res = geek.legint(s1)

# Resulting legendre series
print(res)
