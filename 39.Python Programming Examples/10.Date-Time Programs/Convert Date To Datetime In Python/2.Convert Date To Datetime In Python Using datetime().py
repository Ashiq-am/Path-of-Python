# Importing Modules
from datetime import datetime, date

# Creating Date Objects
MyDate = date(2004, 4, 3) #yyyy/mm/dd

# creating datetime object from year,month and day and time default is midnight
DateTime = datetime(MyDate.year, MyDate.month, MyDate.day)

# Printing Result
print(DateTime)
