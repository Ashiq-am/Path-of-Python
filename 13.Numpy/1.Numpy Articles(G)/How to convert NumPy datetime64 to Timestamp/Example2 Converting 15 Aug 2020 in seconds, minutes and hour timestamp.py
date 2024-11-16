#importing required library
import numpy as np
from datetime import datetime

print("Printing the date:")

# extracting current date in utc format
dt64 = np.datetime64('2020-08-15')

print(dt64)

# converting date time into second timestamp
ts = (dt64 - np.datetime64('1970-01-01T00:00:00Z')) / np.timedelta64(1, 's')
print("Printing the converted datetime in Timestamp in seconds:",
	ts)
print("Printing the converted datetime in Timestamp in minutes")

# converting date time into minute timestamp
tm = (dt64 - np.datetime64('1970-01-01T00:00:00Z')) / np.timedelta64(1, 'm')
print(tm)

print("Printing the converted datetime in Timestamp in hour")

# converting date time into hour timestamp
th = (dt64 - np.datetime64('1970-01-01T00:00:00Z')) / np.timedelta64(1, 'h')
print(th)
