# importing packages
import pandas as pd

# creating a series
s = pd.Series(['Geeks', 'for', 'Geeks'])

# printing the series
print("SERIES")
print(s)

print()

# using convert_dtypes() function
print("AFTER DATATYPE CONVERSION")
print(s.convert_dtypes())
