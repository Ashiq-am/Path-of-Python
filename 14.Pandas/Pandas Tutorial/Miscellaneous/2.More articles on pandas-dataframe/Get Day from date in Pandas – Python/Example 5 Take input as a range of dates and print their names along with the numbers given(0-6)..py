import pandas as pd


myDate = pd.DataFrame({'inputDates':list(pd.date_range('2018-12-30',
													'2019-01-07',
													freq ='D').to_series())})

myDate['inputDates'] = pd.to_datetime(myDate['inputDates'])
myDate['dayOfWeek'] = myDate['inputDates'].dt.dayofweek
myDate['dayOfWeek'] = myDate['inputDates'].dt.day_name()

myDate
