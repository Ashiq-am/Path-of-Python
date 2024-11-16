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

print("DataFrame 1:\n", df1)
print("\nDataFrame 2:\n", df2)
