# import pandas module
import pandas as pd

# Creating two dataframes
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['C', 'B', 'A'], 'another_value': [4, 5, 6]})

# Merging on a common column
result = pd.merge(df1, df2, on='key')

print("Merged DataFrame:")
print(result)
