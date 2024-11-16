# import required packages
import numpy.polynomial.legendre as l

# legfromroots() method generate legendre
# series for given roots
print("Legendre Series-", l.legfromroots((1, 2, 3, 4)))

# Get the datatype
print("Datatype Type - ",l.legfromroots((1, 2, 3, 4)).dtype)

# Get the shape
print("Shape - ",l.legfromroots((1, 2, 3, 4)).shape)
