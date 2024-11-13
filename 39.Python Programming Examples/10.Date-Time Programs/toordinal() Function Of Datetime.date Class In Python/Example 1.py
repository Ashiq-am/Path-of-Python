# Python3 code to demonstrate
# Getting the proleptic Gregorian
# ordinal of a datetime instance

# importing datetime and time module
import datetime
import time

# Getting today's date
todays_Date = datetime.date.fromtimestamp(time.time())

# Calling the toordinal() function over the
# today's date
date = todays_Date.toordinal()

# Printing the proleptic Gregorian ordinal
# for the today's date
print("Proleptic Ordinal for today's date: %s"%date)
