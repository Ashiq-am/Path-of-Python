import pandas as pd
import numpy as np

# Creating a nullable integer array
arr = pd.array([1, 2, None], dtype=pd.Int64Dtype())

# Creating a Series from the nullable integer array
series = pd.Series(arr)

# Printing the Series to see the output
print(series)
