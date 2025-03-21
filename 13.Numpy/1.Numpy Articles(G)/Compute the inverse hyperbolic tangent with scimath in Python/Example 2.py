# import necessary packages
import numpy as np

# Create an input array
x = np.array([1, -1])

# input array before computation
print("Input array->", x)

# compute the inverse hyperbolic tangent using
# arctanh method
print("Resultant Array->", np.emath.arctanh(x))
