# importing datetime and pytz
import datetime
import pytz

# defining the objects
obj1 = datetime.datetime(2001, 11, 15, 1, 20, 25)
obj2 = datetime.datetime(2001, 6, 3, 2, 10, 12)

# Defining the timezone
tz = pytz.timezone('Asia/Kolkata')

# localising the objects to the timezone
obj1 = tz.localize(obj1)
obj2 = tz.localize(obj2)

# printing the differences
print(obj2-obj1)
print(obj1-obj2)

# Checking the object type of the
# difference returned
print(type(obj1-obj2))
