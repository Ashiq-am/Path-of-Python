# importing pandas as pd
import pandas as pd

# Creating an array
array = [11, 21, 8, 18, 65, 84, 32, 10, 5, 24, 32]

# Create the Index
index_ = pd.date_range('2010-10-09', periods = 11, freq ='M')

# Creating the series
# set the index
# set the name
sr = pd.Series.from_array(arr = array, index = index_, name = 'My_series')

# Print the series
print(sr)
