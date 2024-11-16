import pandas as pd

df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [1, 4], 'C': [7, 8]})

merged_df = df1.merge(df2, on='A', how='inner')  # Inner join on column 'A'
summed_df = merged_df.groupby('A').sum()  # Group by 'A' and sum corresponding columns
print(summed_df)
