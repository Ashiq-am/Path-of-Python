# importing pandas as pd
import pandas as pd

# Creating the Series
sr = pd.Series(['2012-4-1', '2019-7-18 12:30', '2008-02-2 10:30',
			'2010-4-22 09:25', '2019-1-1 00:00'])

# Creating the index
idx = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']

# set the index
sr.index = idx

# Convert the underlying data to datetime
sr = pd.to_datetime(sr)

# Print the series
print(sr)
