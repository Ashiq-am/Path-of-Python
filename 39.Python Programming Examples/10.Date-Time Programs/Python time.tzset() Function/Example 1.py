# time.tzset() Function in python

# importin time and os module
import time
import os

# Define TZ environment variable
os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'

# reset the time conversion rules
time.tzset()

# print time
print(time.strftime('%X %x %Z'))

# Define TZ environment variable again
os.environ['TZ'] = 'AEST-10AEDT-11,M10.5.0,M3.5.0'

# reset the time conversion rules
time.tzset()

# print time
print(time.strftime('%X %x %Z'))
