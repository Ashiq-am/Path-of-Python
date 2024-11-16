import numpy as np
from numpy.polynomial import chebyshev

# co.efficient array
c = np.array([[11, 12, 13, 14, 15], [3, 4, 5, 6, 7]])

print(f'The shape of the array is {c.shape}')
print(f'The dimension of the array is {c.ndim}D')
print(f'The datatype of the array is {c.dtype}')

res = chebyshev.chebint(c, m=1, k=5)

# integrated chebyshev series
# with integration constant of 5
print(f'Resultant series ---> {res}')
