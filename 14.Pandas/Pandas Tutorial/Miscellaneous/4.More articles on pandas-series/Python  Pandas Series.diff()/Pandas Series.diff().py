# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# creating list
list = [15, 2, 34, 12, 4, 0, 9, 7]

# creating series
series = pd.Series(list)

# calling method with period 2
period2 = series.diff(2)

# Passing Negative value to period
# passing period of -1
period_1 = series.diff(-1)

# display
print('Diff with period 2:\n{}\n\
Diff with period -1:\n{}'.format(period2, period_1))
