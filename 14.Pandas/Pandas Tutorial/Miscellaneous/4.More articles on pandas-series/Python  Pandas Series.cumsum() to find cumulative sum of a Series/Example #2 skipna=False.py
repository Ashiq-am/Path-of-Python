# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# making list of values
values = [1, 20, 13, np.nan, 0, 1, 5, 23]

# making series from list
series = pd.Series(values)

# calling method
cumsum = series.cumsum(skipna = False)

# display
cumsum
