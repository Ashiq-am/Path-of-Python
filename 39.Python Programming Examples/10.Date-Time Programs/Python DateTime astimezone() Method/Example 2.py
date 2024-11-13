# Python3 code for getting
# a datetime instance according
# to the specified time zone parameter tz

# Importing datetime module
import datetime

# Calling now() function to return
# current datetime
d1 = datetime.datetime.now()

# Calling the astimezone() function without
# any timezone parameter
d2 = d1.astimezone()

# Printing the local current date, time and
# timezone
print(format(d2))
