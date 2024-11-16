# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# creating series 1
series1 = pd.Series([24, 19, 2, 33, 49, 7, np.nan, 10, np.nan])

# creating series 2
series2 = pd.Series([16, np.nan, 2, 23, 5, 40, np.nan, 0, 9])

# setting null replacement value
na_replace = 5

# calling and storing result
result = series1.gt(series2, fill_value = na_replace)

# display
result
