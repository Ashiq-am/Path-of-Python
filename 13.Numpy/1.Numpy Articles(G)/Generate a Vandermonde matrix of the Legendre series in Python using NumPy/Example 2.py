import numpy as np
from numpy.polynomial import legendre

gfg_data = np.array([-1, 2, -3, 4, -5, 6, -7, 8, -9, 10])

# Display Elements of Array
print("Array:\n", gfg_data)

# Display Dimensions of Array
print("\nDimensions:\n", gfg_data.ndim)

# To generate a pseudo Vandermonde
# matrix of the Legendre polynomial
gfg_data = legendre.legvander(gfg_data, 5)
print("\nResult:\n", gfg_data)
