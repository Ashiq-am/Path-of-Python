# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# creating list
list = [1, 0, 12, 1, 0, 4, 22, 0, 3, 9]

# creating series
series = pd.Series(list)

# calling .nonzero() method
result = series.nonzero()

# display
print(result)

# retrieving values using iloc method
values = series.iloc[result]

# display
values
