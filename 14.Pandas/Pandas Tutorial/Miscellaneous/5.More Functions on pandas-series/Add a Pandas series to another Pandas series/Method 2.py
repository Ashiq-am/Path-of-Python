# importing the module
import pandas as pd

# create 2 series objects
series_1 = pd.Series([2, 4, 6, 8])
series_2 = pd.Series([10, 12, 14, 16])

# adding series_2 to series_1 using the concat() function
series_1 = pd.concat([series_1, series_2])

# displaying series_1
print(series_1)
