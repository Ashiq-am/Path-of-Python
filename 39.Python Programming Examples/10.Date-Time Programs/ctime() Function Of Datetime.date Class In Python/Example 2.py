# Python3 code to demonstrate
# Getting a string containing
# the date and time

# Importing datetime module
import datetime

# Initializing a date object for a
# different date
Date = datetime.date(2013, 2, 10)

# Calling the ctime() function
# over the above date
print("The date: %s"%Date.ctime())
