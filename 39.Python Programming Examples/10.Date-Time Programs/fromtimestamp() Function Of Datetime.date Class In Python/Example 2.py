# Python3 code to demonstrate
# Getting a date corresponding
# to a specified timestamp

# Importing datetime and time module
import datetime
import time

# Initializing a timestamp value
Timestamp = 1323456464

# Calling the fromtimestamp() function
# over the above specified Timestamp
date_From_Timestamp = datetime.date.fromtimestamp(Timestamp)

# Printing the date
print("Date for the Timestamp is: %s"%date_From_Timestamp)
