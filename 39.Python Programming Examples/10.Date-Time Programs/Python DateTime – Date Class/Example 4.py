# Python program to
# print current date

from datetime import date

# calling the today
# function of date class
today = date.today()

print("Today's date is", today)

# Converting the date to the string
Str = date.isoformat(today)
print("String Representation", Str)
print(type(Str))
