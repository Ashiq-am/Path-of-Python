# Python program to
# print current date

from datetime import date

# calling the today
# function of date class
today = date.today()

print("Today's date is", today)

# Printing date's components
print("Date components", today.year, today.month, today.day)
