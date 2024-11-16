# importing package
import numpy

# define the polynomials
# p(x) = 2.2
px = (0,0,2.2)

# q(x) = 9.8(x**2) + 4
qx = (9.8,0,4)

# subtract the polynomials
rx = numpy.polynomial.polynomial.polysub(px,qx)

# print the resultant polynomial
print(rx)
