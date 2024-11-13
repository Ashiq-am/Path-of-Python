# Python3 code to demonstrate
# Getting datetime object using a date_string

# importing datetime module
import datetime

# datestring for which datetime_obj required
date_string = 'Sep 01 2021 03:27:05 PM'

# using strptime() to get datetime object
datetime_obj = datetime.datetime.strptime(date_string, '%b %d %Y %I:%M:%S %p')

# Printing datetime
print(datetime_obj)
