# Python program explaining
# numpy.polyfromroots() method

# importing numpy as np
# and numpy.polynomial.polynomial module as geek
import numpy as np
import numpy.polynomial.polynomial as geek

# Input roots

roots = (2, 4, 8)

# using np.polyfromroots() method
res = geek.polyfromroots(roots)

# Resulting polynomial series coefficient
print(res)
