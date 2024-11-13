# Python3 code to demonstrate
# Getting the proleptic Gregorian
# ordinal of a datetime instance

# importing datetime and time module
import datetime
import time

# Getting today's date and time
todays_DateTime = datetime.datetime.now()

# Calling the toordinal() function over the
# today's date and time
DateTime = todays_DateTime.toordinal()

# Printing the proleptic Gregorian ordinal
# for the today's date and time
print("Proleptic Ordinal for today's date and time: %s"%DateTime)
