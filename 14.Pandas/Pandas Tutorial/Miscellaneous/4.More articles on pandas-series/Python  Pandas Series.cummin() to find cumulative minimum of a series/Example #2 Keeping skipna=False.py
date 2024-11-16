# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# making list of values
values = [12, 4, 33, np.nan, 0, 1, 76, 5]

# making series from list
series = pd.Series(values)

# calling method
cummin = series.cummin(skipna=False)

# display
cummin
