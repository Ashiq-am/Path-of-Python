#importing datetime module for now()
from datetime import datetime, timedelta

# using now() to get present_time
present_time = datetime.now()

#time formatting
'{:%H:%M:%S}'.format(present_time)

print("Present time at greenwich meridian is ",end = "")
print( present_time )
