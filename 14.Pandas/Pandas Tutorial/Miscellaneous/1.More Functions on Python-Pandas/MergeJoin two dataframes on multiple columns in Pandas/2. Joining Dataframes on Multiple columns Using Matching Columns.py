import pandas as pd

df1 = pd.DataFrame({'ID': [1, 2, 3],'Order': ['A', 'B', 'C'],'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [1, 2, 4],'Order': ['A', 'B', 'D'],'Amount': [100, 200, 300]})

# Merging on multiple columns ('ID' and 'Order')
merged_df = pd.merge(df1, df2, on=['ID', 'Order'], how='inner')
print(merged_df)