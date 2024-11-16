# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# creating series 1
series1 = pd.Series([11, 0, 2, 43, 9, 27, np.nan, 10, np.nan])

# creating series 2
series2 = pd.Series([16, np.nan, 2, 23, 5, 40, 54, 3, 19])

# NaN replacement
replace_nan = 10

# calling and returning to result variable
result = series1.le(series2, fill_value=replace_nan)

# display
result
