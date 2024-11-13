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
