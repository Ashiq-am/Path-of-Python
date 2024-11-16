# importing pandas module
import pandas as pd
# importing numpy module for generating values
import numpy as np

# using date_range function to generate dates
# from january 1 2021 to march 16 2021 as periods = 75
dates = pd.date_range('1/1/2021', periods=75)

# giving values to dates
results = pd.Series(np.arange(75), index=dates)

# print results
print(results)

# converting to data frame
print(pd.DataFrame(results))
