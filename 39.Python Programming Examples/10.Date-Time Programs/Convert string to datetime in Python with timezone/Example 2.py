# Python3 code to demonstrate
# Getting datetime object using a date_string

# importing datetime module
import datetime

# datestring for which datetime_obj required
date_string = '2021-09-01 15:27:05'

# using strptime() to get datetime object
datetime_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')

# Printing datetime
print(datetime_obj)
