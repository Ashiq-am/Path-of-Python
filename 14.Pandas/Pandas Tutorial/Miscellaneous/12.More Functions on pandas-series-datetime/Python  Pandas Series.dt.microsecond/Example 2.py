# importing pandas as pd
import pandas as pd

# Creating the Series
sr = pd.Series(pd.date_range('2008-2-9 08:20:21',
					periods = 5, freq = '9U'))

# Creating the index
idx = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']

# set the index
sr.index = idx

# Print the series
print(sr)
