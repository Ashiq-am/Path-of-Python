# Python program explaining
# numpy.lagcompanion() method

# importing numpy as np
# and numpy.polynomial.laguerre module as geek
import numpy as np
import numpy.polynomial.laguerre as geek

# Input laguerre series coefficients

s = (2, 4, 8)

# using np.lagcompanion() method
res = geek.lagcompanion(s)

# Resulting Companion matrix
print(res)
