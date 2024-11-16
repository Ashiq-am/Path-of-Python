import numpy as np
import numpy.polynomial.hermite as H

# Create an array of coefficients
c = np.array([[1, 4, 3, 4], [8, 9, 2, 5]])

# coefficient array before differentiation
print("coef array before diff->", c)

# use hermder method to differentiate
# the hermite series
print("coef array after diff->", H.hermder(c, m=2, scl=2, axis=1))
