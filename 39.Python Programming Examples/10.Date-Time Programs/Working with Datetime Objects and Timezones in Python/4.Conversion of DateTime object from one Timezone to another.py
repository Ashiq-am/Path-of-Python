# importing datetime and pytz
import datetime
import pytz

# defining the object and localising it to a timezone
obj = datetime.datetime(2001, 11, 15, 1, 20, 25)
tz = pytz.timezone('Asia/Kolkata')
obj = tz.localize(obj)

# Creating a new timezone
new_tz = pytz.timezone('America/New_York')

# Changing the timezone of our object
new_tz_time = obj.astimezone(new_tz)

# Printing out new time
print(new_tz_time)
