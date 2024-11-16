# importing pandas module
import pandas as pd

# min_count = 0 is the default
pd.Series([]).sum()

# When passed min_count = 1,
# sum of an empty series will be NaN
pd.Series([]).sum(min_count = 1)
