# import chebyshev from numpy.polynomials
# module
from numpy.polynomial import chebyshev

# import complex math module
import cmath

# get the roots for complex numbers
print(chebyshev.chebroots((complex(1, 2),
						complex(2, 3))))

# get the shape
print(chebyshev.chebroots((complex(1, 2),
						complex(2, 3))).shape)

# get the data type
print(chebyshev.chebroots((complex(1, 2),
						complex(2, 3))).dtype)
