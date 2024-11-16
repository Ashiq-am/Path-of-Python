import numpy as np
from numpy.polynomial import chebyshev

# co.efficient array
c = np.array([11, 12, 13, 14, 15])

print(f'The shape of the array is {c.shape}')
print(f'The dimension of the array is {c.ndim}D')
print(f'The datatype of the array is {c.dtype}')

res = chebyshev.chebint(c, m=1, k=3)

# integrated chebyshev series
# with integration constant of 1
print(f'Resultant series ---> {res}')
