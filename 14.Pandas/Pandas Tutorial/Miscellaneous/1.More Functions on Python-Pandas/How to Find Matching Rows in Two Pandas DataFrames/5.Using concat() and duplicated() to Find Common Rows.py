import pandas as pd

# Create the first DataFrame: df1
df1 = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': ['a', 'b', 'c', 'd']
})

# Create the second DataFrame: df2
df2 = pd.DataFrame({
    'A': [3, 4, 5, 6],
    'B': ['c', 'd', 'e', 'f']
})

# Concatenate the two DataFrames
concatenated_df = pd.concat([df1, df2])

# Find duplicated rows (i.e., rows that appear in both DataFrames)
matching_rows = concatenated_df[concatenated_df.duplicated(keep=False)].drop_duplicates()

print(matching_rows)