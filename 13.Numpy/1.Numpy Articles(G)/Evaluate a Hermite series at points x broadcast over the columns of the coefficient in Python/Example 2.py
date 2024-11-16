import numpy as np
from numpy.polynomial import hermite

a = np.array([[1,2,3,4,5],[6,7,8,9,10]])

# Dimensions of Array
print("\nDimensions of Array:\n",a.ndim)

# Shape of the array
print("\nShape of Array:\n",a.shape)

# Tuple
x = [6,7,8,9,10]

# To evaluate a Hermite series at
# points x broadcast over the columns
hermite.hermval(x,a,tensor=True)
