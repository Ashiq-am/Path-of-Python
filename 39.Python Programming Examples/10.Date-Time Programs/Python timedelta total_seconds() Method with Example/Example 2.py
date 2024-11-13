# Python3 code for getting
# total seconds for the
# given duration of time

# Importing time and timedelta module
from datetime import time, timedelta

# Specifing a time duration
A = timedelta(minutes=-3 * 13)

# Calling the total_seconds() function
# over the specified time duration
totalsecond = A.total_seconds()

# Getting the Total seconds for
# the duration of -3*13 minutes
print("Total seconds in -3*13 minutes:", totalsecond)
