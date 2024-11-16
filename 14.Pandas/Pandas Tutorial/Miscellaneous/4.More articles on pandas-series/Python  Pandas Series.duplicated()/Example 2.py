# importing pandas as pd
import pandas as pd

# Creating the Series
sr = pd.Series([11, 11, 8, 18, 65, 18, 32, 10, 5, 32, 32])

# Create the Index
index_ = pd.date_range('2010-10-09', periods = 11, freq ='M')

# set the index
sr.index = index_

# Print the series
print(sr)
