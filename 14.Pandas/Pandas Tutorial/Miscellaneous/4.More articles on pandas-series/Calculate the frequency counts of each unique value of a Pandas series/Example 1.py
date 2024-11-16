# importing the module
import pandas as pd

# creating the series
s = pd.Series(data = [2, 3, 4, 5, 5, 6,7, 8, 9, 5, 3])

# displaying the series
print(s)

# finding the unique count
print(s.value_counts())
