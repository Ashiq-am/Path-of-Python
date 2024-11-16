# Python program explaining
# numpy.legdiv() method

# importing numpy as np
# and numpy.polynomial.legendre module as geek
import numpy as np
import numpy.polynomial.legendre as geek

# Legendre series coefficients

s1 = (2, 4, 8)
s2 = (1, 3, 5)

# using np.legdiv() method
res = geek.legdiv(s1, s2)

# Resulting legendre series
print(res)
