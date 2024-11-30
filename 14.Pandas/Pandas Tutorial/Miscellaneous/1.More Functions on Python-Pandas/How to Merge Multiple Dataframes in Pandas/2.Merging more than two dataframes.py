import pandas as pd
from functools import reduce

df1 = pd.DataFrame({'id': [1, 2, 3],'name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'id': [2, 3, 4],'age': [30, 24, 28]})
df3 = pd.DataFrame({'id': [1, 3, 4],'score': [85, 90, 75]})
dfs = [df1, df2, df3]

# Using reduce to merge all DataFrames on 'id'
merged_df = reduce(lambda left, right: pd.merge(left, right, on='id', how='outer'), dfs)
print(merged_df)