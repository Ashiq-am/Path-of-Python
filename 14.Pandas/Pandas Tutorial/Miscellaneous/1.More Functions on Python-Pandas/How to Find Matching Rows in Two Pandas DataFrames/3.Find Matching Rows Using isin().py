import pandas as pd

# Create the first DataFrame: df1
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Flower': ['Rose', 'Lily', 'Tulip', 'Daisy']
})

# Create the second DataFrame: df2
df2 = pd.DataFrame({
    'ID': [3, 4, 7],
    'Category': ['Outdoor', 'Outdoor', 'Indoor']
})

# Find rows in df1 where 'ID' matches with 'ID' in df2
matching_rows = df1[df1['ID'].isin(df2['ID'])]
print(matching_rows)