# Python program explaining
# numpy.legroots() method

# importing numpy as np
# and numpy.polynomial.legendre module as geek
import numpy as np
import numpy.polynomial.legendre as geek

# Input legendre series coefficients

s = (2, 4, 8)

# using np.legroots() method
res = geek.legroots(s)

# Resulting legendre series coefficient
print(res)
