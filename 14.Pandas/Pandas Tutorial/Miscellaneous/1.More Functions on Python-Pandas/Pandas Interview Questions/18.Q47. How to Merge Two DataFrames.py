import pandas as pd
# Create two DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3],
'B': [4, 5, 6]},
index=[10, 20, 30])

df2 = pd.DataFrame({'C': [7, 8, 9],
'D': [10, 11, 12]},
index=[20, 30, 40])

# Merge both dataframe
result = pd.merge(df1, df2, left_index=True, right_index=True)
print(result)
