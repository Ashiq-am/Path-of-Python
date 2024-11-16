# Python program explaining
# numpy.legfromroots() method

# importing numpy as np
# and numpy.polynomial.legendre module as geek
import numpy as np
import numpy.polynomial.legendre as geek

# Input roots

roots = (2, 4, 8)

# using np.legfromroots() method
res = geek.legfromroots(roots)

# Resulting legendre series coefficient
print(res)
