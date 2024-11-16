# Python program explaining
# numpy.lagfromroots() method

# importing numpy as np
# and numpy.polynomial.laguerre module as geek
import numpy as np
import numpy.polynomial.laguerre as geek

# Input roots
s = (1, 2, 3, 4, 5)

# using np.lagfromroots() method
res = geek.lagfromroots(s)

# Resulting laguerre series coefficient
print(res)
