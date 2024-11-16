# importing pandas as pd
import pandas as pd

# Creating a Series
df = pd.Series([1, 2, 3, 4, 5, 10, 11, 21, 4])

# This will prefix 'Row_' in
# each row of the series
df = df.add_prefix('Row_')

# Print the Series
df
