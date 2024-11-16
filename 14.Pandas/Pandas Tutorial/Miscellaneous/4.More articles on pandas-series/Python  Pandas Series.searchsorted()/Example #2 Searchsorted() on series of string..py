# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# creating list
data = ['apple', 'banana', 'mango', 'pineapple', 'pizza']

# creating series
series = pd.Series(data)

# values to be inserted
val = ['grapes', 'watermelon']

# calling .searchsorted() method
result = series.searchsorted(value=val)

# display
result
