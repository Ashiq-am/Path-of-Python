# import pandas module
import pandas as pd

# Create the first DataFrame
df1 = pd.DataFrame({
    'A': [1, 2, 3, 4],
}, index=['a', 'b', 'c', 'd'])

# Create the second DataFrame
df2 = pd.DataFrame({
    'B': [5, 6, 7, 8],
}, index=['b', 'c', 'd', 'e'])

# merging dataframe based on common index
merged_df = pd.merge(df1, df2, left_index=True, right_index=True, how='inner')
print("Merged DataFrame:\n", merged_df)
