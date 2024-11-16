import numpy as np
from numpy.polynomial import legendre

# co.efficient array
c = np.array([[11, 12, 13, 14, 15],
			[56, 55, 44, 678, 89]])

print(f'The shape of the array is {c.shape}')
print(f'The dimension of the array is {c.ndim}D')
print(f'The datatype of the array is {c.dtype}')

res = legendre.legint(c, lbnd=-1)

# integrated legendre series
# with lbnd=-1
print(f'Resultant series ---> {res}')
