# import chebyshev
from numpy.polynomial import chebyshev

# create a complex variable
my_value = complex(4,5)

# display value
print("Complex value: ", my_value)

# generate chebyshev roots
print("chebyshev roots: ", chebyshev.chebfromroots((-my_value, my_value)))
