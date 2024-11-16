# Python program explaining
# numpy.lagfromroots() method

# importing numpy as np
# and numpy.polynomial.laguerre module as geek
import numpy as np
import numpy.polynomial.laguerre as geek

# Input roots

roots = (2, 4, 8)

# using np.lagfromroots() method
res = geek.lagfromroots(roots)

# Resulting laguerre series coefficient
print(res)
