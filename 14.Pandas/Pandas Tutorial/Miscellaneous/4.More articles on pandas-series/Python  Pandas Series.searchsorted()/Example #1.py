# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# creating list
list = [0, 2, 3, 7, 12, 12, 15, 24]

# creating series
series = pd.Series(list)

# values to be inserted
val = [1, 7, 14]

# calling .searchsorted() method
result = series.searchsorted(value=val)

# display
result
