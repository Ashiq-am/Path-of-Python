# import necessary packages
import numpy as np
import numpy.polynomial.laguerre as L

# Create an array of coefficients
c = np.array([1, 5, 0, 4])

# Display the array before differentiation
print("Array before passing to lagder->", c)

# differentiate a Laguerre series for m times
print("After differentiation->", L.lagder(c, 2, scl=2))
