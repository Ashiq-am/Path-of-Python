import pandas as pd


date = pd.DataFrame({'inputDates':['1999-7-14', '1998-12-14',
								'2001-01-18', '2020-07-18',
								'2006-01-8'],
					'inputVals':[1, 2, 3, 4, 5]})

date['inputDates'] = pd.to_datetime(date['inputDates'])
date['dayOfWeek'] = date['inputDates'].dt.dayofweek
days = {0:'Mon', 1:'Tues', 2:'Wed', 3:'Thurs', 4:'Fri', 5:'Sat', 6:'Sun'}
date['dayOfWeek'] = date['dayOfWeek'].apply(lambda x: days[x])

date
