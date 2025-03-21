# time.tzset() Function in python

# importin time and os module
import time
import os

# Define TZ environment variable
os.environ['TZ'] = 'Australia/Melbourne'

# reset the time conversion rules
time.tzset()

# print time
print(time.strftime('%X %x %Z'))


# Define TZ environment variable again
os.environ['TZ'] = 'Egypt'

# reset the time conversion rules
time.tzset()

# print time
print(time.strftime('%X %x %Z'))
