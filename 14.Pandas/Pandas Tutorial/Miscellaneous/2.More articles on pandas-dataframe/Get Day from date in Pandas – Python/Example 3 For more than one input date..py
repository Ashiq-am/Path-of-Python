import pandas as pd


date = pd.DataFrame({'inputDates':['2015-01-07', '2015-12-02',
								'2005-01-03', '2016-11-13',
								'2020-06-03'],
					'inputVals':[1, 2, 3, 4, 5]})

date['inputDates'] = pd.to_datetime(date['inputDates'])
date['dayOfWeek'] = date['inputDates'].dt.day_name()

date
