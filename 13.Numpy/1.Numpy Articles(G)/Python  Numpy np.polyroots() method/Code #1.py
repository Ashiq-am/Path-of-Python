# Python program explaining
# numpy.polyroots() method

# importing numpy as np
# and numpy.polynomial.polynomial module as geek
import numpy as np
import numpy.polynomial.polynomial as geek

# Input polynomial series coefficients

s = (2, 4, 8)

# using np.polyroots() method
res = geek.polyroots(s)

# Resulting polynomial series coefficient
print(res)
