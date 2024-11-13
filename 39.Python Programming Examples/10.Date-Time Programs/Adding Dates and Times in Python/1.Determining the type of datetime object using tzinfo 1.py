# importing the required modules
import datetime
import pytz

# instantiate datetime object
obj = datetime.datetime.now()

# specifying the timezone using pytz library
tzone = pytz.timezone("America/Los_Angeles")

# localizing the datetime object
datetime_obj = tzone.localize(obj)

# extracting time zone info of the object
print(datetime_obj.tzinfo)
