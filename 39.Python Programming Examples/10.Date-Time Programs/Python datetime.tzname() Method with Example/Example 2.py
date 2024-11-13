# import datetime module
from datetime import datetime

# import pytz module
import pytz

# get the datetime of the present
dt = datetime.now()

# Tzinfo is missing from the time object
print(dt)

# display tz info for the dt
print(dt.tzinfo)
print("Timezone:", dt.tzname())
print()

# Adding a timezone for asia /kolkate
timezone = pytz.timezone("Asia/Kolkata")

# getting the timezone using localize method
mydt = timezone.localize(dt)

print(mydt)

# getting the time zone info using tzinfo method
print("Tzinfo:", mydt.tzinfo)

# display time zone name using tzname
print("Timezone name:", mydt.tzname())
