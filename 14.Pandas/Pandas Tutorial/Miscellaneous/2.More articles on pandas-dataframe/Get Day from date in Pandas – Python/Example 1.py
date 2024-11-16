import pandas as pd


date = pd.date_range('2018-12-30', '2019-01-07',
					freq='D').to_series()
date.dt.dayofweek
