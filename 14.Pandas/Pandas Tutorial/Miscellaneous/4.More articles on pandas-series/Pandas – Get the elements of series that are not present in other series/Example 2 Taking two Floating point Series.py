# Importing pandas library
import pandas as pd

# Creating 2 pandas Series
ps1 = pd.Series([2.8, 4.5, 8.0, 2.2, 10.1, 4.7, 9.9])
ps2 = pd.Series([1.4, 2.8, 4.7, 4.8, 10.1, 9.9, 50.12])

print("Series1:")
print(ps1)
print("\nSeries2:")
print(ps2)

# Using Bitwise NOT operator along
# with pandas.isin()
print("\nItems of ps1 not present in ps2:")
res = ps1[~ps1.isin(ps2)]
print(res)
