# Python3 code to demonstrate
# Getting a tuple of ISO Year,
# ISO Week Number and ISO Weekday

# Importing date module from datetime
from datetime import date

# Creating an instance for
# different dates
A = date(2020, 10, 11)

# Calling the isocalendar() function
# over the above specified date
Date = A.isocalendar()

# Printing Original date and its
# ISO Year, ISO Week Number
# and ISO Weekday
print("Original date:",A)
print("Date in isocalendar is:", Date)
