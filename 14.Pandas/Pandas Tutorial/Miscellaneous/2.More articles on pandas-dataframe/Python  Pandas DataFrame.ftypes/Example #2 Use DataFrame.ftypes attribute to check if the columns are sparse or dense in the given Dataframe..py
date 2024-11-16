# importing pandas as pd
import pandas as pd

# Create an array
arr = [100, 35, 125, 85, 35]

# Creating a sparse DataFrame
df = pd.SparseDataFrame(arr)

# Print the DataFrame
print(df)
