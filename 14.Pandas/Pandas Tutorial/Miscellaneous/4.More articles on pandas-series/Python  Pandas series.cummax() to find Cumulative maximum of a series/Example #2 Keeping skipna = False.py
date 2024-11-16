# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# making list of values
values = [9, 4, 33, np.nan, 0, 1, 76, 5]

# making series from list
series = pd.Series(values)

# calling method
cummax = series.cummax(skipna=False)

# display
cummax
