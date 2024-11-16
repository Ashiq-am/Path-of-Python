# Importing pandas library
import pandas as pd

# Creating 2 pandas Series
ps1 = pd.Series([2.5, 4, 6, 8, 10, 1.75, 40])
ps2 = pd.Series([1.5, 3, 5, 7, 10, 1.75, 20])

print("Series1:")
print(ps1)
print("\nSeries2:")
print(ps2)

# Comparing two series using Series.equals()
# function
print("\nResult of comparing Two Series:")
result = ps1.equals(other=ps2)
print(result)
