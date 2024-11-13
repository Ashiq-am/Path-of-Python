# Python3 code to demonstrate working of
# Get Month Name from Month Number
# Using strftime() + %B
from datetime import datetime

# initializing date
test_date = datetime(2020, 4, 8)

# printing original date
print("The original date is : " + str(test_date))

# getting month name using %B
res = test_date.strftime("%B")

# printing result
print("Month Name from Date : " + str(res))
