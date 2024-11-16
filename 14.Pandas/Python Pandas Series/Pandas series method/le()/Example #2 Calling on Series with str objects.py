# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# creating series 1
series1 = pd.Series(['A', 0, 'c', 43, 9, 'e', np.nan, 'x', np.nan])

# creating series 2
series2 = pd.Series(['v', np.nan, 'c', 23, 5, 'D', 54, 'p', 19])

# NaN replacement
replace_nan = 10

# calling and returning to result variable
result = series1.le(series2, fill_value=replace_nan)

# display
result
