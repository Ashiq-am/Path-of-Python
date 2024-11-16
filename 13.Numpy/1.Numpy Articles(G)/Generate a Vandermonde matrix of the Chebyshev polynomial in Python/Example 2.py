import numpy as np
from numpy.polynomial import chebyshev

gfg = np.array([59,89,45,71,56])

# Print array
print("Array - ", gfg)

# Print dimension of the array
print("Dimension of Array:-",gfg.ndim)

# Print Datatype array
print("Datatype of Array:-",gfg.dtype)

# Print shape array
print("Shape of Array:-",gfg.shape)

# Generate a Vandermonde matrix of the
# Chebyshev polynomial of degree 5
gfg_matrix=chebyshev.chebvander(gfg, 5)
print('\n',gfg_matrix)

# Print shape martrix
print("\nShape of Martix:-\n",gfg_matrix.shape)
