# Importing Modules
from datetime import datetime, date, time

# Creating Date Objects
MyDate = date(1998, 9, 24) #yyyy/mm/dd

# Creating Time Objects
MyTime = time(10, 12, 30) #hr/min/sec

# Combining Date and Time objects
DateTime = datetime.combine(MyDate, MyTime)

# Printing Result
print(DateTime)
