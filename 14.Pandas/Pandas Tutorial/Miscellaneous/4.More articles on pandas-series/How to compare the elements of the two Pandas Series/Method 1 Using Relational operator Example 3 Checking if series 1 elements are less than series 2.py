# Importing pandas library
import pandas as pd

# Creating 2 pandas Series
ps1 = pd.Series([2.5, 4, 6, 8, 10, 1.75, 40])
ps2 = pd.Series([1.5, 3, 5, 7, 10, 1.75, 20])

print("Series1:")
print(ps1)
print("\nSeries2:")
print(ps2)

# Compare the series using '<' Relational operators
print("\nCompare the elements of the two given Series:")
print("\nLess than:")
print(ps1 < ps2)
