# Python3 code for getting
# the Gregorian date corresponding
# to a given Gregorian ordinal.

# Importing datetime module
import datetime

# Specifing a Gregorian ordinal
ordinal = 123456

# Calling the fromordinal() function
# over the specified Gregorian ordinal
date = datetime.date.fromordinal(ordinal)

# Printing the Gregorian date
print("The Gregorian date for the Gregorian\
ordinal %d is: %s"%(ordinal, date))
