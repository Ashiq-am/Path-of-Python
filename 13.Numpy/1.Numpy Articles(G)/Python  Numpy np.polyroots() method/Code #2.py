# Python program explaining
# numpy.polyroot() method

# importing numpy as np
# and numpy.polynomial.polynomial module as geek
import numpy as np
import numpy.polynomial.polynomial as geek

# polynomial series coefficients
s = (1, 2, 3, 4, 5)

# using np.polyroots() method
res = geek.polyroots(s)

# Resulting polynomial series
print(res)
