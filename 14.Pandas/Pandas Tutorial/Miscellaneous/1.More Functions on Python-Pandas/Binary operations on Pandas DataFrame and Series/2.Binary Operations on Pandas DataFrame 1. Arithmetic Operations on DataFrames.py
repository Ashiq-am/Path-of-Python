import pandas as pd
df1 = pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60]})
df2 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Subtracting the DataFrames
result = df1 - df2
print(result)