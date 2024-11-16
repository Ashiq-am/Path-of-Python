# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# creating list
list = [5, 12, 1, 0, 4, 22, 15, 3, 9]

# creating series
series = pd.Series(list)

# calling .mad() method
result = series.mad()

# display
result
