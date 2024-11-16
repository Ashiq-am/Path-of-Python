# importing pandas as pd
import pandas as pd

# generating all dates in given range
# with increment by days
allDates = pd.date_range('2020-06-27', '2020-08-03', freq ='W')

# converting dates to series
series = allDates.to_series()

series.dt.week
