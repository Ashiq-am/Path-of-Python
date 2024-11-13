# import module
from datetime import date

# Creating an instance
# of datetime
Date = date(2010, 2, 12)
print("Original date : ", Date)

# Using replace() method
New_date = Date.replace(month=5)
print("After Modify the month:", New_date)
