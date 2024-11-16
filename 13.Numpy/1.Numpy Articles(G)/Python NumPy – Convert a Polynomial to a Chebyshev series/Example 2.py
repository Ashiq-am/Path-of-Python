# import package
from numpy import polynomial as P

# converting polynomial to chebyshev series
poly = P.Polynomial(range(10))
print("polynomial to chebyshev series : ",
	poly.convert(kind=P.Chebyshev))
