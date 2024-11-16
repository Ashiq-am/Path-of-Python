import numpy as np
from numpy.polynomial import hermite

# co.efficient array
c = np.arange(32).reshape(2, 2, 4, 2)

print(f'The co.efficient array is {c}')
print(f'The shape of the array is {c.shape}')
print(f'The dimension of the array is {c.ndim}D')
print(f'The datatype of the array is {c.dtype}')

# evaluating 4d co.eff array with a 3d hermite series
res = hermite.hermgrid3d([1, 2], [1, 2], [1, 2], c)

# resultant array
print(f'Resultant series ---> {res}')
