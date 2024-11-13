# importing datetime module
from datatime import datetime

# now is a method in datetime module is
# used to retrieve current data,time
myobj = datetime.now()


# printing the object itself
print("Object:", myobj)

# printing current hour using hour
# class
print("Current hour ", myobj.hour)

# printing current minute using minute
# class
print("Current minute ", myobj.minute)

# printing current second using second
# class
print("Current second ", myobj.second)

# printing current microsecond using microsecond
# class
print("Current microsecond ", myobj.microsecond)
