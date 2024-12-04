import numpy as np
import pandas as pd

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Ensure arrays have the same length
if len(array1) != len(array2):
    raise ValueError("Arrays must have the same length")

# Create DataFrame with specified column names
df = pd.DataFrame({'Column1': array1, 'Column2': array2})

print(df)