# importing pandas as pd
import pandas as pd

# Creating the Series
sr = pd.Series(pd.date_range('2019-1-1 12:30', periods = 5, freq = 'H',
							tz = 'Asia / Calcutta'))

# Creating the index
idx = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']

# set the index
sr.index = idx

# Print the series
print(sr)
