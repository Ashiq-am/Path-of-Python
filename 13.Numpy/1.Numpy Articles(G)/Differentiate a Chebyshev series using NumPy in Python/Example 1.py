import numpy as np
from numpy.polynomial import chebyshev

# co.efficient array
c = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 11])

print(f'The shape of the array is {c.shape}')
print(f'The dimension of the array is {c.ndim}D')
print(f'The datatype of the array is {c.dtype}')

res = chebyshev.chebder(c, m=1, scl=1)

# differentiated chebyshev series with
# first order derivated and scale 1
print(f'Resultant series ---> {res}')
