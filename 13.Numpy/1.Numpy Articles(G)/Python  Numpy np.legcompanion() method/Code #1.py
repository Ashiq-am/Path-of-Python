# Python program explaining
# numpy.legcompanion() method

# importing numpy as np
# and numpy.polynomial.legendre module as geek
import numpy as np
import numpy.polynomial.legendre as geek

# Input legendre series coefficients

s = (2, 4, 8)

# using np.legcompanion() method
res = geek.legcompanion(s)

# Resulting Companion matrix
print(res)
