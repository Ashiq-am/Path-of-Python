# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# making list of values
values = [2, 10, np.nan, 4, 3, 0, 1]

# making series from list
series = pd.Series(values)

# calling method
cumprod = series.cumprod()

# display
cumprod
