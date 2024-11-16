# import pandas library
import pandas as pd

# create a series
sr = pd.Series(pd.date_range('2020-7-20 12:41',
                             periods=5,
                             freq='min'))

# create a pandas dataframe with a
# column having timestamps
df = pd.DataFrame(dict(time_stamps=sr))

# view the created dataframe
print(df)
