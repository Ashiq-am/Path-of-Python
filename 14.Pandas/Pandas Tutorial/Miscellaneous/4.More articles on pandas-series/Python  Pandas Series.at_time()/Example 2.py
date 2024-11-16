# importing pandas as pd
import pandas as pd

# Creating the Series
sr = pd.Series([11, 21, 8, 18, 65, 18, 32, 10, 5, 32, None])

# Create the Index
# apply monthly frequency
index_ = pd.date_range('2010-10-09 08:45', periods = 11, freq ='M')

# set the index
sr.index = index_

# Print the series
print(sr)
