import numpy as np
from numpy.polynomial import chebyshev

# co.efficient array
c = np.arange(27).reshape(3, 3, 3)

print(f'The co.efficient array is {c}')
print(f'The shape of the array is {c.shape}')
print(f'The dimension of the array is {c.ndim}D')
print(f'The datatype of the array is {c.dtype}')

# evaluating co.eff array with a chebyshev series
res = chebyshev.chebgrid2d([2, 2], [2, 2], c)

# resultant array
print(f'Resultant series ---> {res}')
