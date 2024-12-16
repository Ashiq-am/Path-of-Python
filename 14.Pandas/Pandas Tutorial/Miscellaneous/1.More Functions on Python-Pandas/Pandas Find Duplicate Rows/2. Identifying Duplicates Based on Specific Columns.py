# Find duplicates based on 'Name' and 'Age' columns
duplicates_by_columns = df[df.duplicated(subset=['Name', 'Age'])]
print(duplicates_by_columns)