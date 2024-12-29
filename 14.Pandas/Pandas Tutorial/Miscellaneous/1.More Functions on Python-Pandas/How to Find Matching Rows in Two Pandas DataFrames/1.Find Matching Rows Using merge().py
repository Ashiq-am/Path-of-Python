import pandas as pd

# Sample DataFrames
df1 = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': ['a', 'b', 'c', 'd']
})

df2 = pd.DataFrame({
    'A': [3, 4, 5, 6],
    'B': ['c', 'd', 'e', 'f']
})

# Merge dataframes on columns 'A' and 'B' (default is inner join)
matching_rows = pd.merge(df1, df2, on=['A', 'B'], how='inner')
print(matching_rows)