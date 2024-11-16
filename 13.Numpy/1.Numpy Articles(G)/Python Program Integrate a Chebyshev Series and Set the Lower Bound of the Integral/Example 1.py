import numpy as np
from numpy.polynomial import chebyshev

# co.efficient array
c = np.array([3, 5, 7, 9])

print(f'The shape of the array is {c.shape}')
print(f'The dimension of the array is {c.ndim}D')
print(f'The datatype of the array is {c.dtype}')

res = chebyshev.chebint(c, m=1, k=1, lbnd=-2)

# integrated chebyshev series with lower bound of -2
print(f'Resultant series ---> {res}')
