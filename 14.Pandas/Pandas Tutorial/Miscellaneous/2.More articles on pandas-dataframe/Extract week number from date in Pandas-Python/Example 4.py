# importing pandas as pd
import pandas as pd

# generating the series
dates = pd.Series(pd.date_range('2020-2-10',
								periods = 5,
								freq ='M'))

# converting to dataframe
df = pd.DataFrame({'date_given': dates})

# extracting the week number
df['week_number'] = df['date_given'].dt.week

df
