import numpy as np
from numpy.polynomial import chebyshev

# co.efficient array
c = np.array([11, 12, 13, 14, 15])

print(f'The shape of the array is {c.shape}')
print(f'The dimension of the array is {c.ndim}D')
print(f'The datatype of the array is {c.dtype}')

res = chebyshev.chebint(c, lbnd=-2)

# integrated chebyshev series
# with lbnd=-2
print(f'Resultant series ---> {res}')
