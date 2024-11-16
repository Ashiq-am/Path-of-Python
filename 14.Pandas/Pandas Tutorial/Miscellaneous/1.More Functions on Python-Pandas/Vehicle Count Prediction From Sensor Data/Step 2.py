# function to get all data fron time stamp

# get date
from turtle import pd

import train as train


def get_dom(dt):
	return dt.day

# get week day
def get_weekday(dt):
	return dt.weekday()

# get hour
def get_hour(dt):
	return dt.hour

# get year
def get_year(dt):
	return dt.year

# get month
def get_month(dt):
	return dt.month

# get year day
def get_dayofyear(dt):
	return dt.dayofyear

# get year week
def get_weekofyear(dt):
	return dt.weekofyear


train['DateTime'] = train['DateTime'].map(pd.to_datetime)
train['date'] = train['DateTime'].map(get_dom)
train['weekday'] = train['DateTime'].map(get_weekday)
train['hour'] = train['DateTime'].map(get_hour)
train['month'] = train['DateTime'].map(get_month)
train['year'] = train['DateTime'].map(get_year)
train['dayofyear'] = train['DateTime'].map(get_dayofyear)
train['weekofyear'] = train['DateTime'].map(get_weekofyear)

# display
train.head()
