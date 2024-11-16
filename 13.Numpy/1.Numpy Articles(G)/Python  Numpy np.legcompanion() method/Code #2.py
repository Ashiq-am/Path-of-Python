# Python program explaining
# numpy.legcompanion() method

# importing numpy as np
# and numpy.polynomial.legendre module as geek
import numpy as np
import numpy.polynomial.legendre as geek

# legendre series coefficients
s = (1, 2, 3, 4, 5)

# using np.legcompanion() method
res = geek.legcompanion(s)

# Resulting Companion matrix
print(res)
