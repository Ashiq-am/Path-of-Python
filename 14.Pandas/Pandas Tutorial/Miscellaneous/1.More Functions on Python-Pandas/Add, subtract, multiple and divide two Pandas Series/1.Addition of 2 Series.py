# importing the module
import pandas as pd

# creating 2 Pandas Series
series1 = pd.Series([1, 2, 3, 4, 5])
series2 = pd.Series([6, 7, 8, 9, 10])

# adding the 2 Series
series3 = series1 + series2

# displaying the result
print(series3)
