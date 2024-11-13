# importing required modules
from datetime import datetime
import pytz

# creating a datetime object
curr_datetime = datetime.now()
print("Current timezone")
print(curr_datetime)

# creating timezone using pytz package
changed_timezone = pytz.timezone('US/Pacific')

# replacing timezone using the specified timezone value
curr_datetime = curr_datetime.replace(tzinfo=changed_timezone)
curr_datetime = curr_datetime.astimezone(changed_timezone)
print("Replaced timezone")
print(curr_datetime)
