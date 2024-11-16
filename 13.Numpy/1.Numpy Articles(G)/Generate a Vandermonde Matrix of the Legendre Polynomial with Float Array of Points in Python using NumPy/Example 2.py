import numpy as np
from numpy.polynomial import legendre

gfg_data = np.array([-1.57,0.58, -3.57, 1.44, 2.75,
				-8.97,7.45,-0.56,-4.74,3.33])

# Display Elements of Array
print("Array:\n",gfg_data)

# Display Dimensions of Array
print("\nDimensions:\n",gfg_data.ndim)

# To generate a pseudo Vandermonde
# matrix of the Legendre polynomial
gfg_data=legendre.legvander(gfg_data, 5)
print("\nResult:\n",gfg_data)
