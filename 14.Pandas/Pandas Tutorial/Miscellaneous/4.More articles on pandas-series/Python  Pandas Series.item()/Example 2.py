# importing pandas as pd
import pandas as pd

# Creating the Series
sr = pd.Series([11])

# Create the Index
index_ = pd.date_range('2010-10-09', periods = 1, freq ='M')

# set the index
sr.index = index_

# Print the series
print(sr)
