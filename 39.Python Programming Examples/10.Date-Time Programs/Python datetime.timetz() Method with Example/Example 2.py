# Python3 code for getting
# a time object with the same
# specified hour, minute, second,
# microsecond, fold and tzinfo.

# Importing datetime module
import datetime

# Creating a current datetime instance
A = datetime.datetime.now()

# Calling the timetz() function over
# the above current datetime instance
B = A.timetz()

# Printing the original current date time object
print("Original current date time object:", A)

# Printing the new current time object
print("New current time object:", B)
