# Python3 code to demonstrate
# Getting Ordinal value using
# toordinal().

# importing datetime module for today()
import datetime

# using date.today() to get todays date
dateToday = datetime.date.today()

# Using toordinal() to generate ordinal vale.
toOrdinal = dateToday.toordinal()

# Prints Ordinal Value of Todays Date.
print(f"Ordinal of date {dateToday} is {toOrdinal}")
