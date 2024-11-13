# Importing Modules
from datetime import datetime

# Creating string variable and writing date in it
MyDate = "2003-12-17"

# creating datetime object from string and time default is midnight
DateTime = datetime.strptime(MyDate, "%Y-%m-%d")

# Printing Result
print(DateTime)
