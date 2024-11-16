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

# finding common index using
common_index_set = set(df1.index) & set(df2.index)
print("Common Index (Set Operation):", common_index_set)
