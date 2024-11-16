# Import numpy library
import numpy as np

# Create a numpy array
arr = np.array([1e-90, 1e-100])

# Applying the function
rslt = np.log1p(arr)

print(rslt)
