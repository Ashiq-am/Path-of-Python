# import the library
import pandas as pd

# create the Series
s = pd.Series([2.2 + 1j])
print(s)

# fetching the absolute values
print("\nThe absolute values are :")
print(s.abs())
