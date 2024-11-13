# Python3 code to demonstrate
# Getting the proleptic Gregorian
# ordinal of a datetime instance

# importing datetime and time module
import datetime
import time

# Initializing a date and time
DateTime = datetime.datetime(1358, 8, 12, 1, 3, 4, 9)

# Calling the toordinal() function over the
# above date and time
Date_Time = DateTime.toordinal()

# Printing the proleptic Gregorian ordinal
# for the above given date and time
print("Proleptic Ordinal for today's date and time: %s"%Date_Time)
