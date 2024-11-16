# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# creating series 1
series1 = pd.Series([70, 5, 0, 225, 1, 16, np.nan, 10, np.nan])

# creating series 2
series2 = pd.Series([70, np.nan, 2, 23, 1, 95, 53, 10, 5])

# NaN replacement
replace_nan = 5

# calling and returning to result variable
result = series1.eq(series2, fill_value=replace_nan)

# display
result
