# importing pandas as pd
import pandas as pd

# Creating the Series
sr = pd.Series(['2012-10-21 09:30:45', '2019-7-18 12:30:21', '2008-02-2 10:30:38',
			'2010-4-22 09:25:19', '2019-11-8 02:22:44'])

# Creating the index
idx = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']

# set the index
sr.index = idx

# Convert the underlying data to datetime
sr = pd.to_datetime(sr)

# Print the series
print(sr)
