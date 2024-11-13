# Python3 code to illustrate the addition
# of time onto the datetime object

# Importing datetime
import datetime

# Initializing a date and time
date_and_time = datetime.datetime(2021, 8, 22, 11, 2, 5)

print("Original time:")
print(date_and_time)

# Calling the timedelta() function and
# adding 2 minutes and 10 seconds
time_change = datetime.timedelta(minutes=2, seconds=10)
new_time = date_and_time + time_change

# Printing the new datetime object
print("changed time:")
print(new_time)
