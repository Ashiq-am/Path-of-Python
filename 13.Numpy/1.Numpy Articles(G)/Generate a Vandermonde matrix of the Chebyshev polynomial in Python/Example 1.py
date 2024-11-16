import numpy as np
from numpy.polynomial import chebyshev

gfg = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Print array
print("Array - ", gfg)

# Print dimension of the array
print("Dimension of Array:-", gfg.ndim)

# Print Datatype array
print("Datatype of Array:-", gfg.dtype)

# Print shape array
print("Shape of Array:-", gfg.shape)

# Generate a Vandermonde matrix of the
# Chebyshev polynomial of degree 2
gfg_matrix = chebyshev.chebvander(gfg, 2)
print('\n', gfg_matrix)

# Print shape martrix
print("\nShape of Martix:-\n", gfg_matrix.shape)
