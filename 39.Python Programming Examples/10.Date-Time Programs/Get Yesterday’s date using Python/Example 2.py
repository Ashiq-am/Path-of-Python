# Python program to get
# Yesterday's date


# Import date and timdelta class
# from datetime module
from datetime import date
from datetime import timedelta


# Get today's date
today = date.today()
print("Today is: ", today)

# Get 2 days earlier
yesterday = today - timedelta(days = 2)
print("Day before yesterday was: ", yesterday)
