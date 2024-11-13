# Python3 code to demonstrate
# Getting date values in ISO 8601 format

# importing datetime and time module
import datetime
import time

# Getting today's date
todays_Date = datetime.date.fromtimestamp(time.time())

# Calling the isoformat() function over the
# today's date
date_in_ISOFormat = todays_Date.isoformat()

# Printing Today's date in ISO format
print("Today's date in ISO Format: %s" % date_in_ISOFormat)
