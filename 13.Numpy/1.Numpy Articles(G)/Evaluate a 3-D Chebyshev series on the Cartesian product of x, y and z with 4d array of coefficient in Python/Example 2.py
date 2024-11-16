import numpy as np
from numpy.polynomial import chebyshev

# co.efficient array
c = np.arange(64).reshape(4, 4, 2, 2)

print(f'The co.efficient array is \n{c}\n')
print(f'The shape of the array is \n{c.shape}\n')
print(f'The dimension of the array is \n{c.ndim}D\n')
print(f'The datatype of the array is \n{c.dtype}\n')

# evaluating 4d co.eff array with a 3d chebyshev series
res = chebyshev.chebgrid3d([2, 1], [2, 1], [2, 1], c)

# resultant array
print(f'Resultant series ---> {res}')
