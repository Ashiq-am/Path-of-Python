# Python3 code to demonstrate
# Getting date and time values
# in ISO 8601 format

# importing datetime and time module
import datetime
import time

# Getting today's date and time
todays_Date = datetime.datetime.now()

# Calling the isoformat() function over the
# today's date and time
DateTime_in_ISOFormat = todays_Date.isoformat()

# Printing Today's date and time in ISO format
print("Today's date and time in ISO Format: %s" % DateTime_in_ISOFormat)
