# import the library
import pandas as pd

# create the Series
s = pd.Series([pd.Timedelta('2 days')])
print(s)

# fetching the absolute values
print("\nThe absolute values are :")
print(s.abs())
