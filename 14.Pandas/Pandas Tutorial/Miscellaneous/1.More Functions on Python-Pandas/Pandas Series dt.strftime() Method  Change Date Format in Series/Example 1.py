import pandas as pd
sr = pd.Series(['2012-12-31 08:45', '2019-1-1 12:30', '2008-02-2 10:30',
			'2010-1-1 09:25', '2019-12-31 00:00'])
idx = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']
sr.index = idx
sr = pd.to_datetime(sr)
result = sr.dt.strftime('% B % d, % Y, % r')
print(result)
