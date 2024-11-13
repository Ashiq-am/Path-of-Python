# Python3 code to demonstrate
# Getting a tuple of ISO Year,
# ISO Week Number and ISO Weekday

# Importing date module from datetime
from datetime import date

# Calling the today() function
# to return todays date
Todays_date = date.today()

# Printing today's date
print(Todays_date)

# Calling the isocalendar() function
# over the above today's date to return
# its ISO Year, ISO Week Number
# and ISO Weekday
print(Todays_date.isocalendar())
