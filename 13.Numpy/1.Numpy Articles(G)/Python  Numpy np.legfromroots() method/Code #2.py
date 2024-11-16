# Python program explaining
# numpy.legfromroots() method

# importing numpy as np
# and numpy.polynomial.legendre module as geek
import numpy as np
import numpy.polynomial.legendre as geek

# Input roots
s = (1, 2, 3, 4, 5)

# using np.legfromroots() method
res = geek.legfromroots(s)

# Resulting legendre series coefficient
print(res)
