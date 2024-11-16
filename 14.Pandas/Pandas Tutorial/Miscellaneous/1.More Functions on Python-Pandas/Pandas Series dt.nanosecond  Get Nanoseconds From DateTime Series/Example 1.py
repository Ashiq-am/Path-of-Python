import pandas as pd
sr = pd.Series(pd.date_range('2012-12-12 12:12', periods = 5, freq = '5N'))
idx = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']
sr.index = idx
result = sr.dt.nanosecond
print(result)
