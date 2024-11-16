# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# creating series 1
series1 = pd.Series([70, 5, 0, 225, 1, 16, np.nan, 10, np.nan])

# creating series 2
series2 = pd.Series([27, np.nan, 2, 23, 1, 95, 53, 10, 5])

# combining and returning results to variable
# calling on series1
result1 = series1.combine_first(series2)

# calling on series2
result2 = series2.combine_first(series1)

# printing result
print('Result 1:\n', result1, '\n\nResult 2:\n', result2)
