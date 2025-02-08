import pandas as pd
df1 = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6]})
df2 = pd.DataFrame({'A': [1, None, 3], 'B': [None, 5, 6]})

# Adding the DataFrames
result = df1 + df2
print(result)