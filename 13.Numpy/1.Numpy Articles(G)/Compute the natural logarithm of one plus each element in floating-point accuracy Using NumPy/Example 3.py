# Import numpy library
import numpy as np

# Create a numpy array
arr = np.array([1, 1e-1, 3, 1e-0])

# Applying the function
rslt = np.log1p(arr)

print(rslt)
