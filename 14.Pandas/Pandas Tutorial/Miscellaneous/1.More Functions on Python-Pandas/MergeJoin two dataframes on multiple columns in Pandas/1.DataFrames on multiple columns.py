import pandas as pd

df1 = pd.DataFrame({'ID': [1, 2, 3],'Name': ['Alice', 'Bob', 'Charlie'],'Score': [85, 90, 95]})
df2 = pd.DataFrame({'ID': [1, 2, 4],'Name': ['Alice', 'Bob', 'David'],'Grade': ['A', 'B', 'C']})

# Merge on multiple columns
merged_df = pd.merge(df1, df2, on=['ID', 'Name'], how='inner')
print(merged_df)
