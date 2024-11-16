# code
import numpy as np

# Example array
array = np.array([1, 2, np.nan, 4, 5])

# Check for NaN values
nan_check = np.isnan(array)
print(nan_check)
