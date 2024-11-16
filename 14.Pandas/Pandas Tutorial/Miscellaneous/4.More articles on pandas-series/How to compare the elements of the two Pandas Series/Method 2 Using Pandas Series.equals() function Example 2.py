# Importing pandas library
import pandas as pd

# Creating 2 pandas Series
ps1 = pd.Series([80, 25, 3, 25, 24, 6])
ps2 = pd.Series([80, 25, 3, 25, 24, 6])

print("Series1:")
print(ps1)
print("\nSeries2:")
print(ps2)

# Comparing two series using Series.equals()
# function
print("\nResult of comparing Two Series:")
result = ps1.equals(other=ps2)
print(result)
