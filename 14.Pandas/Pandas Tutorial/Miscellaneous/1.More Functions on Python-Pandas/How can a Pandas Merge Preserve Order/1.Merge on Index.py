# import pandas module
import pandas as pd

# Creating two dataframes
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
df2 = pd.DataFrame({'C': [4, 5, 6], 'D': ['x', 'y', 'z']})

# Merging on index
result = pd.merge(df1, df2, left_index=True, right_index=True)

print("Merged DataFrame:")
print(result)
