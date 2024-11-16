# import legendre method
from numpy.polynomial import legendre

# polynomial.legendre.legroots()
# method to compute roots
print(legendre.legroots((0, 1, 2, 3, 4, 5, 6)))

# return the datatype
print(legendre.legroots((0, 1, 2, 3, 4, 5, 6)).dtype)

# return the shape
print(legendre.legroots((0, 1, 2, 3, 4, 5, 6)).shape)
