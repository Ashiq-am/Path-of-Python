# import module
from datetime import date

# Creating an instance
# of datetime
Date = date(2010, 2, 12)
print("Original date : ", Date)

# Using replace() method
New_date = Date.replace(day=21)
print("After Modify the day:", New_date)
