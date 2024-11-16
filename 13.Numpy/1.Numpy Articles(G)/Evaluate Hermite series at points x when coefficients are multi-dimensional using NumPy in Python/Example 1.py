import numpy as np
from numpy.polynomial import hermite

# coefficient array
c = np.array([[11, 12], [13, 14]])

print(f'The coefficient array is {c}')
print(f'The shape of the array is {c.shape}')
print(f'The dimension of the array is {c.ndim}D')
print(f'The datatype of the array is {c.dtype}')

# evaluating multidimensal array of hermiteseries
res = hermite.hermval([1, 2], c)

# resultant array
print(f'Resultant series ---> {res}')
