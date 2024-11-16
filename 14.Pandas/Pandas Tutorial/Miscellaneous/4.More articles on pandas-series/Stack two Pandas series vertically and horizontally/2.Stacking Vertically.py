# importing the module
import pandas as pd

# creating the series
series1 = pd.Series(['g', 'e', 'e', 'k', 's'])
print("Series 1:")
print(series1)
series2 = pd.Series([9, 8, 7, 6, 5])
print("Series 2:")
print(series2)

# stacking the series vertically
df = pd.concat([series1, series2], axis = 0)
print("\nStack two series vertically:")
display(df)
