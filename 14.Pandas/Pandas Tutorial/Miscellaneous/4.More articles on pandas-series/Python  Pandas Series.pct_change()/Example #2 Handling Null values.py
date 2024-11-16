# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# creating list
list = [10, np.nan, 14, 20, 25, 12.5, 13, 0, 50]

# creating series
series = pd.Series(list)

# calling method
result = series.pct_change(fill_method='bfill')

# display
result
