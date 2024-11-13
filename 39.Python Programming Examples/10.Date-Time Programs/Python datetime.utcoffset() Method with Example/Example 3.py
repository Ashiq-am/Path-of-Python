# Python3 code for getting
# the difference between the
# local time and UTC time

# Importing datetime and pytz module
from datetime import datetime
import pytz

# Calling the now() function to
# get current date and time
naive = datetime.now()

# adding a timezone
timezone = pytz.timezone("Asia/Tokyo")
aware1 = timezone.localize(naive)

# Calling the utcoffset() function
# over the above localized time
print("Time ahead of UTC by:", aware1.utcoffset())
