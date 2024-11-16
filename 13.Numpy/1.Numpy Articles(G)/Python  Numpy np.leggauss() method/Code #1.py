# Python program explaining
# numpy.leggauss() method

# importing numpy as np
# and numpy.polynomial.legendre module as geek
import numpy as np
import numpy.polynomial.legendre as geek

# Input degree = 2

degree = 2

# using np.leggauss() method
res = geek.leggauss(degree)

# Resulting array of sample point and weight
print(res)
