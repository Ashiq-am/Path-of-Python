# import necessary packages
import cmath
import numpy.polynomial.legendre as l

# legfromroots() method generate legendre
# series for given roots
print("Legendre Series-", l.legfromroots((complex(1, 1), 2)))
