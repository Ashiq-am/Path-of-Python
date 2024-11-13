# Python3 code to demonstrate working of
# Count date on weekday in Year Range
# Using sum() + generator expression
from datetime import datetime

# initializing date
date = 13

# initializing weekday
weekdy = 5

# initializing range of Years
strt, end = 1950, 2020

# printing Number
print("The date, weekday : " + str(date) + " " + str(weekdy))

# sum performs accumulation
res = sum(datetime(year, month, date).weekday() == weekdy
		for year in range(strt, end + 1) for month in range(1, 13))

# printing result
print("Total dates with same weekday : " + str(res))
