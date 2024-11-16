from numpy.polynomial import chebyshev

# consider the coefficient
j = complex(2)

# datatype
print(chebyshev.chebroots((-j, j)).dtype)

# shape
print(chebyshev.chebroots((-j, j)).shape)

# get the roots of chebyshev series
print(chebyshev.chebroots((-j, j)))
