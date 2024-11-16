# import pandas library
import pandas as pd

# create a series
sr = pd.Series(['2020-7-20 12:41',
                '2020-7-20 12:42',
                '2020-7-20 12:43',
                '2020-7-20 12:44'])

# convert the series to datetime
sr = pd.to_datetime(sr)

# create a pandas dataframe with a
# column having timestamps
df = pd.DataFrame(dict(time_stamps=sr))

# view the created dataframe
print(df)
