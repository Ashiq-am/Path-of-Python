from numpy.polynomial import chebyshev

# consider the coefficient
j = complex(1,3)
print(j)

# datatype
print(chebyshev.chebroots((-j, j)).dtype)

# shape
print(chebyshev.chebroots((-j, j)).shape)

# get the roots of chebyshev series
print(chebyshev.chebroots((-j, j)))
