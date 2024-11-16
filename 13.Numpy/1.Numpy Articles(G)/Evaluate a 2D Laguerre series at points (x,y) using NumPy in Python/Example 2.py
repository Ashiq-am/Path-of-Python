import numpy as np
from numpy.polynomial import laguerre

# co.efficient array
c = np.array([[1,2,3,4,5],[45,56,65,55,55]])

print(f'The co.efficient array is {c}')
print(f'The shape of the array is {c.shape}')
print(f'The dimension of the array is {c.ndim}D')
print(f'The datatype of the array is {c.dtype}')

# evaluating coeff array with a laguerre series
res = laguerre.lagval2d([2, 2], [2, 2], c)

# resultant array
print(f'Resultant series ---> {res}')
