import pandas as pd

sr = pd.Series(['2012-10-21 09:30', '2019-7-18 12:30', '2008-02-2 10:30',
				'2010-4-22 09:25', '2019-11-8 02:22'])
idx = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']

# set the index
sr.index = idx
sr = pd.to_datetime(sr)
print(sr)
