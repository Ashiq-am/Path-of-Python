# Python program to
# print current date

from datetime import date

# calling the today
# function of date class
today = date.today()

# Getting Weekday using weekday()
# method
print("Weekday using weekday():", today.weekday())

# Getting Weekday using isoweekday()
# method
print("Weekday using isoweekday():", today.isoweekday())

# Getting the proleptic Gregorian
# ordinal
print("proleptic Gregorian ordinal:", today.toordinal())

# Getting the date from the ordinal
print("Date from ordinal", date.fromordinal(737000))
