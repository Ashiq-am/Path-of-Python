# import chebyshev from numpy.polynomials
# module
from numpy.polynomial import chebyshev


# get the roots for normal numbers
print(chebyshev.chebroots((-1, 0, 1, 2, 3)))

# get the data type
print(chebyshev.chebroots((-1, 0, 1, 2, 3)).dtype)

# get the shape
print(chebyshev.chebroots((-1, 0, 1, 2, 3)).shape)
