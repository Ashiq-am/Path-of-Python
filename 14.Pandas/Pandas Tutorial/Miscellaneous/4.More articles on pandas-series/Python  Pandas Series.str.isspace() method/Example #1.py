# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# creating series 1
series1 = pd.Series(['a', 'b', ' ', ' c ', 'd', ' ', np.nan])

# checking for all space elements in series1
result1 = series1.str.isspace()

# display
print('Series 1 results:\n\n', result1)
