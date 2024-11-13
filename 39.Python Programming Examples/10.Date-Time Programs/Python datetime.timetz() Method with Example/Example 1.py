# Python3 code for getting
# a time object with the same
# specified hour, minute, second,
# microsecond, fold and tzinfo.

# Importing datetime module
import datetime

# Creating a datetime instance
A = datetime.datetime(2021, 8, 3, 10, 11, 12, 13)

# Calling the timetz() function over
# the above datetime instance
B = A.timetz()

# Printing the original date time object
print("Original date time object:", A)

# Printing the new time object
print("New time object:", B)
