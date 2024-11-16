# Importing required libraries
import pandas as pd
import numpy as np
import datetime

# Making a dataframe which will
# have two columns two store different dates
df= pd.DataFrame({'dates1': np.array(
[datetime.datetime(2000, 10, 19), datetime.datetime(2021, 1, 8)]),
				'dates2': np.array(
					[datetime.datetime(1998, 6, 20),
					datetime.datetime(2012, 10, 18)] )})

# Used to convert the difference in terms of weeks
df['Number_of_weeks'] = ((df.dates1 - df.dates2)/np.timedelta64(1, 'W'))
df['Number_of_weeks'] = df['Number_of_weeks'].astype(int)
print(df)
