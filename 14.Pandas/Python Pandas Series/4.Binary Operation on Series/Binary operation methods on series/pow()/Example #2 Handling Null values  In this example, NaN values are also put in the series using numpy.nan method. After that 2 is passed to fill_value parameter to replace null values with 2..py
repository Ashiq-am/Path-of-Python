# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# creating first series
first =[1, 2, 5, 6, 3, np.nan, 4, np.nan]

# creating second series
second =[5, np.nan, 3, 2, np.nan, 1, 3, 2]

# making series
first = pd.Series(first)

# making seriesa
second = pd.Series(second)

# value for null replacement
null_replacement = 2

# calling .pow()
result = first.pow(second, fill_value = null_replacement)

# display
result
