# Python3.7 code for Getting
# a date object from a specified
# string that contains date in
# ISO format. i.e., yyyy-mm-dd

# Importing datetime module
import datetime

# Initializing a date
Date = "2012-10-12"

# Calling fromisoformat() function to
# construct a datetime.date object
New_date = datetime.date.fromisoformat(Date)

# Printing the new constructed date object
print("The constructed date object is: %s"%New_date)
