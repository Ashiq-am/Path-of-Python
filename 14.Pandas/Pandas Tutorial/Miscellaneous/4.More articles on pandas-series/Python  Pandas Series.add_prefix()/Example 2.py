# importing pandas as pd
import pandas as pd

# Creating the Series
sr = pd.Series([51, 10, 24, 18, 1, 84, 12, 10, 5, 24, 0])

# Create the Index
# apply yearly frequency
index_ = pd.date_range('2010-10-09 08:45', periods = 11, freq ='Y')

# set the index
sr.index = index_

# Print the series
print(sr)
