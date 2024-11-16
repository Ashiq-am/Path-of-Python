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

# finding common index using intersection()
common_index = df1.index.intersection(df2.index)

# Filter df1 by common index
df1_filtered = df1.loc[common_index]

# Filter df2 by common index
df2_filtered = df2.loc[common_index]

print("Filtered DataFrame 1:\n", df1_filtered)
print("\nFiltered DataFrame 2:\n", df2_filtered)
