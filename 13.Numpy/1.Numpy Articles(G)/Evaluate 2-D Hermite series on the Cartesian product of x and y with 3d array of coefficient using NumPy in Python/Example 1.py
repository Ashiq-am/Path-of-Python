import numpy as np
from numpy.polynomial import hermite

# coefficient array
c = np.arange(24).reshape(2,2,6)

print(f'The coefficient array is {c}')
print(f'The shape of the array is {c.shape}')
print(f'The dimension of the array is {c.ndim}D')
print(f'The datatype of the array is {c.dtype}')

# evaluating 3d coeff array with a 2d
# hermite series
res = hermite.hermgrid2d([2,1], [2,1], c)

# resultant array
print(f'Resultant series ---> {res}')
