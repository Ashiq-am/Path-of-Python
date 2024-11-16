import pandas as pd


date = pd.DataFrame({'inputDate':['2020-07-07']})
date['inputDate'] = pd.to_datetime(date['inputDate'])
date['dayOfWeek'] = date['inputDate'].dt.day_name()

date
