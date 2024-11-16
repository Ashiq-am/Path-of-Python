# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# creating series 1
series1 = pd.Series([11, 21, 2, 43, 9, 27, np.nan, 110, np.nan])

# creating series 2
series2 = pd.Series([16, np.nan, 2, 23, 5, 40, np.nan, 0, 19])

# setting null replacement value
na_replace = 10

# calling and storing result
result = series1.lt(series2, fill_value = na_replace)

# display
result
