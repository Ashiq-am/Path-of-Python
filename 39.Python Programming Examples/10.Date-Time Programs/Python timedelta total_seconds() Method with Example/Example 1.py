# Python3 code for getting
# total seconds for the
# given duration of time

# Importing time and timedelta module
from datetime import time, timedelta

# Specifing a time duration
A = timedelta(minutes=55)

# Calling the total_seconds() function
# over the specified time duration
totalsecond = A.total_seconds()

# Getting the Total seconds for
# the duration of 55 minutes
print("Total seconds in 55 minutes:", totalsecond)
