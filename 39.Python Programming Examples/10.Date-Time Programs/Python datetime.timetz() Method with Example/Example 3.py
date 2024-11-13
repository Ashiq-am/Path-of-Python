# Python3 code for getting
# a time object with the same
# specified hour, minute, second,
# microsecond, fold and tzinfo.

# Importing datetime module
import datetime

# Creating datetime instances
A = datetime.timedelta(hours=12, minutes=12)
obj = datetime.timezone(A, name="IST")
B = datetime.datetime(2012, 1, 2, 3, 10, 15, 20, obj)

# Calling the timetz() function over the above
# specified datetime
C = B.timetz()

# Printing the Original datetime object
print("Original datetime object:", B)

# Printing the time object with tzinfo attributes
print("Time object with tzinfo attributes:", C)

# Printing the time object without tzinfo attributes
print("Time object without tzinfo attributes:", B.time())
