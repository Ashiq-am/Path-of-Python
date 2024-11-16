# Python program explaining
# numpy.legadd() method

# importing numpy as np
# and numpy.polynomial.legendre module as geek
import numpy as np
import numpy.polynomial.legendre as geek

# Legendre series coefficients
s1 = (1, 3, 5)
s2 = (2, 4, 6)

# using np.legadd() method
res = geek.legadd(s1, s2)

# Resulting legendre series
print(res)
