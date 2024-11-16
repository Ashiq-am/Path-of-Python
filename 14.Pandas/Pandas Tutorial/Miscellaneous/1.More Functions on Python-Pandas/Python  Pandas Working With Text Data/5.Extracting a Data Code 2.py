# importing pandas module
import pandas as pd

# creating a series
s = pd.Series(['a1', 'b2', 'c3'])

# Extracting a data
n = s.str.extract(r'(?P<Geeks>[ab])(?P<For>\d)')

print(n)
