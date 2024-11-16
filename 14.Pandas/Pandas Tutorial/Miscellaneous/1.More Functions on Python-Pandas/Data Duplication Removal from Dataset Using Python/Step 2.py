# Identify duplicate records
duplicate_mask = df.duplicated()
duplicates = df[duplicate_mask]
print(duplicates)
