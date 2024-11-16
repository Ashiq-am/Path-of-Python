# import pandas module
import pandas as pd

# Creating two dataframes
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
df2 = pd.DataFrame({'A': [4, 5, 6], 'B': ['d', 'e', 'f']})

# Concatenating dataframes
result = pd.concat([df1, df2])

print("Concatenated DataFrame:")
print(result)
