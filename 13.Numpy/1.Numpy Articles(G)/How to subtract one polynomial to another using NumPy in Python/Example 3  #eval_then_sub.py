# importing package
import numpy

# define the polynomials
# p(x) = (5/3)x
px = (0,5/3,0)

# q(x) = (-7/4)(x**2) + (9/5)
qx = (-7/4,0,9/5)

# subtract the polynomials
rx = numpy.polynomial.polynomial.polysub(px,qx)

# print the resultant polynomial
print(rx)
