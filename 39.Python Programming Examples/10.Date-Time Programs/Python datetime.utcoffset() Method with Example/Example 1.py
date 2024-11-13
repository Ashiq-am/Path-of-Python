# Python3 code for getting
# the difference between the
# local time and UTC time

# Importing datetime and pytz module
from datetime import datetime
import pytz

# Calling the now() function to get
# current date and time
date_time = datetime.now()

# Calling the utcoffset() function
# over the above intitialized datetime
print(date_time.utcoffset())
