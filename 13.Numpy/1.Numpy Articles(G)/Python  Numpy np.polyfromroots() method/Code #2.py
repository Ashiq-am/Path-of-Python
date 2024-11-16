# Python program explaining
# numpy.polyfromroots() method

# importing numpy as np
# and numpy.polynomial.polynomial module as geek
import numpy as np
import numpy.polynomial.polynomial as geek

# Input roots
s = (1, 2, 3, 4, 5)

# using np.polyfromroots() method
res = geek.polyfromroots(s)

# Resulting polynomial series coefficient
print(res)
