# import pandas library
import pandas as pd

# create s series of all sundays
result = pd.Series(pd.date_range('2020-01-01',
								periods = 52,
								freq = 'W-SUN'))
print("All Sundays in 2020:")

# show the series
print(result)
