# Python3 code for getting
# the Gregorian date corresponding
# to a given Gregorian ordinal.

# Importing datetime module
import datetime

# Calling the fromordinal() function over
# the 1st day of Gregorian calendar as its parameter
date = datetime.date.fromordinal(1)

# Printing the Gregorian date for the 1st date
# of Gregorian calendar
print("Gregorian Date for the 1st day \
of Gregorian calendar: %s"%date)
