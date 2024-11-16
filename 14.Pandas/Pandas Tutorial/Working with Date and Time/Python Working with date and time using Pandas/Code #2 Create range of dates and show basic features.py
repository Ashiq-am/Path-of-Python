# Create date and time with dataframe
from turtle import pd

from pandas import datetime

data = pd.date_range('1/1/2011', periods = 10, freq ='H')

x = datetime.now()
x.month, x.year
