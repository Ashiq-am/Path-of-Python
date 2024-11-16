# importing pandas module
import pandas as pd

# min_count = 0 is the default
pd.Series([]).prod()

# When passed min_count = 1,
# product of an empty series will be NaN
pd.Series([]).prod(min_count = 1)
