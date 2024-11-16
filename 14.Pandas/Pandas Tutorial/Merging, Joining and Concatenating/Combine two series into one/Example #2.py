# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# creating first series
first =[1, 2, np.nan, 5, 6, 3, np.nan, 7, 11, 0, 4, 8]

# creating second series
second =[5, 3, 2, np.nan, 1, 3, 9, 21, 3, np.nan, 1, np.nan]

# making series
first = pd.Series(first)

# making seriesa
second = pd.Series(second)

# calling .combine() method
result = first.combine(second, func =(lambda x1, x2: x1 if x1 > x2 else x2), fill_value = 5)

# display
result
