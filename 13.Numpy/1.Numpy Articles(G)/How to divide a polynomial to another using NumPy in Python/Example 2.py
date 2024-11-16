# importing package
import numpy

# define the polynomials
# p(x) = (x**2) + 3x + 2
px = (1,3,2)

# g(x) = x + 1
gx = (1,1,0)

# divide the polynomials
qx,rx = numpy.polynomial.polynomial.polydiv(px,gx)

# print the result
# quotiient
print(qx)

# remainder
print(rx)
