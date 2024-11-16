# import numpy library
import numpy as np


# enter the coefficients of poly
# in the array
p = np.poly1d([1, 3, 2, 1])

# multiplying by r(or roots) to get
# the roots
root_of_poly = p.r
print(root_of_poly)
