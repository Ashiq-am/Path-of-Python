import numpy as np
from numpy.polynomial import hermite

# coefficient array
c = np.array([1, 2, 3, 4, 5])

print(f'The co.efficient array is {c}')
print(f'The shape of the array is {c.shape}')
print(f'The dimension of the array is {c.ndim}D')
print(f'The datatype of the array is {c.dtype}')

# evaluating 1d co.eff array with a 2d
# hermite series
res = hermite.hermgrid2d([1, 2], [1, 2], c)

# resultant array
print(f'Resultant series ---> {res}')
