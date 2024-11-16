# Convert the Time column to datatime format
from turtle import pd

from pandas.tests.test_downstream import df

df['Time'] = pd.to_datetime(df.Time)

df.head()
