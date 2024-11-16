import numpy as np
from numpy.polynomial import hermite

# co.eff array
c = np.arange(27).reshape(3, 3, 3)

print(f'The co.efficient array is {c}')
print(f'The shape of the array is {c.shape}')
print(f'The dimension of the array is {c.ndim}D')
print(f'The datatype of the array is {c.dtype}')

# evaluating multidimensal array of hermiteseries
res = hermite.hermval([17, 22], c)

# resultant array
print(f'Resultant series ---> {res}')
