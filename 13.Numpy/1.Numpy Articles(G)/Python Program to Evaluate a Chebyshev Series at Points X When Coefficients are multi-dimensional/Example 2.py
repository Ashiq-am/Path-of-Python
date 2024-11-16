import numpy as np
from numpy.polynomial import chebyshev

# multidimensional array of coefficients
c = np.arange(9).reshape(3, 3, 1)

print(f'The shape of the array is {c.shape}')
print(f'The dimension of the array is {c.ndim}D')
print(f'The datatype of the array is {c.dtype}')

# pass the points to evaluate at x to the chebval function
res = chebyshev.chebval([11, 12], c, tensor=True)

# chebshev series evaluated at point [1,2]
print(f'Resultant series ---> {res}')
