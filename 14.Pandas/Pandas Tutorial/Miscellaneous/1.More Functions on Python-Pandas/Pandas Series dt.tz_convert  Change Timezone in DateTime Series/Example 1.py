import pandas as pd
sr = pd.Series(pd.date_range('2012-12-31 00:00', periods = 5, freq = 'D',
							tz = 'US / Central'))
idx = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']
sr.index = idx
result = sr.dt.tz_convert(tz = 'Europe / Berlin')
print(result)
