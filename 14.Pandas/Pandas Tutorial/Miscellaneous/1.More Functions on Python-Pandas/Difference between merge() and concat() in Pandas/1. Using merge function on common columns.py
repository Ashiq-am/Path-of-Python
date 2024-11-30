import pandas as pd

df1 = pd.DataFrame({'ID': [1, 2, 3],'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4],'Age': [25, 30, 35]})

# Merge dataframes on 'ID'
merged_df = pd.merge(df1, df2, on='ID', how='inner')
print("Merged DataFrame (using merge):")
print(merged_df)

# Concatenating the two dataframes along columns (axis=1)
concat_df = pd.concat([df1, df2], axis=1)
print("\nConcatenated DataFrame (using concat):")
print(concat_df)