# Python3 code for getting
# total seconds for the
# given duration of time

# Importing time and timedelta module
from datetime import time, timedelta

# Specifing a time duration
A = timedelta(days=2, hours=3,
              minutes=43,
              seconds=35)

# Calling the total_seconds() function
# over the specified time duration
totalsecond = A.total_seconds()

# Getting the Total seconds
print("Total seconds are:", totalsecond)
