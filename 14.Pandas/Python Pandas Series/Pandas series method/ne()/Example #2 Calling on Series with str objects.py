# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# creating series 1
series1 = pd.Series(['Aaa', 0, 'cat', 43, 9, 'Dog', np.nan, 'x', np.nan])

# creating series 2
series2 = pd.Series(['vaa', np.nan, 'Cat', 23, 5, 'Dog', 54, 'x', np.nan])

# NaN replacement
replace_nan = 14

# calling and returning to result variable
result = series1.ne(series2, fill_value=replace_nan)

# display
result
