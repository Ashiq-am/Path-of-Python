import numpy as np
from numpy.polynomial import chebyshev

# co.efficient array
c = np.array([[3, 5, 7, 9], [21, 22, 23, 24]])

print(f'The shape of the array is {c.shape}')
print(f'The dimension of the array is {c.ndim}D')
print(f'The datatype of the array is {c.dtype}')

res = chebyshev.chebint(c, m=3, k=3, lbnd=-10)

# integrated chebyshev series with lower bound of -10
print(f'Resultant series ---> {res}')
