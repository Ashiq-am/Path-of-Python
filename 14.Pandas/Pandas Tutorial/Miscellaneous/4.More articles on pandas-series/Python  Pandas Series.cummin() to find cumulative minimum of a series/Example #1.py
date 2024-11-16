# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# making list of values
values = [3, 4, np.nan, 7, 2, 0]

# making series from list
series = pd.Series(values)

# calling method
cummin = series.cummin()

# display
cummin
