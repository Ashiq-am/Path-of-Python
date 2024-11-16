# Check for empty cells using boolean indexing along columns (axis=1)
empty_columns = df.isnull().all(axis=0)
print(empty_columns)
