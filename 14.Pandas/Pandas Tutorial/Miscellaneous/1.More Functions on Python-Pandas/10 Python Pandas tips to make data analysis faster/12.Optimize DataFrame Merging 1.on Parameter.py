import pandas as pd
# Sample DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Value1': ['A', 'B', 'C']})
df2 = pd.DataFrame({'ID': [1, 2, 3], 'Value2': ['X', 'Y', 'Z']})
# Explicitly specifying the 'on' parameter
merged_df = pd.merge(df1, df2, on='ID')
print(merged_df)
