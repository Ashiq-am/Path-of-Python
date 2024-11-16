import numpy as np
from numpy.polynomial import chebyshev

# co.efficient array
c = np.array([[[11, 12, 13, 14, 15],
			[3, 4, 5, 6, 7],
			[21, 22, 23, 24, 25]]])

print(f'The shape of the array is {c.shape}')
print(f'The dimension of the array is {c.ndim}D')
print(f'The datatype of the array is {c.dtype}')

res = chebyshev.chebint(c, m=5, k=5, lbnd=-20)

# integrated chebyshev series with lower bound of -20
print(f'Resultant series ---> {res}')
