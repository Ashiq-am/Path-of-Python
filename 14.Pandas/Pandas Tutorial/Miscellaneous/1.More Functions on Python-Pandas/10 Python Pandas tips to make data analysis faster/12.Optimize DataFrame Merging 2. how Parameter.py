import pandas as pd
# Sample DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Value1': ['A', 'B', 'C']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Value2': ['X', 'Y', 'Z']})
# Explicitly specifying the 'how' parameter
merged_df_inner = pd.merge(df1, df2, on='ID', how='inner')
merged_df_outer = pd.merge(df1, df2, on='ID', how='outer')
print("Inner Merge:")
print(merged_df_inner)
print("\nOuter Merge:")
print(merged_df_outer)
