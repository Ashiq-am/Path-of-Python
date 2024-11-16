import numpy as np
from numpy.polynomial import legendre

gfg_data = np.array([-1,2,-3,4,-5])

# Display Elements of Array
print("Array:\n",gfg_data)

# Display Dimensions of Array
print("\nDimensions:\n",gfg_data.ndim)

# To generate a pseudo Vandermonde
# matrix of the Legendre polynomial
gfg=legendre.legvander(gfg_data, 2)
print("\nResult:\n",gfg_data)
