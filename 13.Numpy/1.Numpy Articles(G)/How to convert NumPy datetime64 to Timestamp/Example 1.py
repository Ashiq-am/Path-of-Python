# importing required library
import numpy as np
from datetime import datetime

# extracting current date
# in utc format
date = datetime.utcnow()

print("Printing the Current date:",
	date)

# converting the current date
# in datetime64 format
date64 = np.datetime64(date)

# converting date time into second timestamp
ts = (date64 - np.datetime64('1970-01-01T00:00:00Z')) / np.timedelta64(1, 's')

print("Printing the converted datetime in Timestamp in seconds:",
	ts)

# converting date time into minute timestamp
tm = (date64 - np.datetime64('1970-01-01T00:00:00Z')) / np.timedelta64(1, 'm')

print("Printing the converted datetime in Timestamp in minutes:",
	ts)

# converting date time into hour timestamp
th = (date64 - np.datetime64('1970-01-01T00:00:00Z')) / np.timedelta64(1, 'h')

print("Printing the converted datetime in Timestamp in hour:",
	th)
