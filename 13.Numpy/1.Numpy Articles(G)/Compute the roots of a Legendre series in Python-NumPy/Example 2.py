# import legendre method
from numpy.polynomial import legendre

# polynomial.legendre.legroots() method to
# compute roots using complex no.
print(legendre.legroots([-1 + 9j, 2 - 77j,
						31 - 25j, 40 - 311j,
						72 + 11j]))

# return the datatype
print(legendre.legroots((0, 1)).dtype)

# return the shape
print(legendre.legroots((0, 1)).shape)
