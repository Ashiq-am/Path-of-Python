# Python program explaining
# numpy.laggauss() method

# importing numpy as np
# and numpy.polynomial.laguerre module as geek
import numpy as np
import numpy.polynomial.laguerre as geek

# Input degree
degree = 3

# using np.laggauss() method
res = geek.laggauss(degree)

# Resulting array of sample point and weight
print(res)
