# import important module
import datetime
from datetime import datetime

# Create datetime string
datetime_str = "10JAN300123000"

# call datetime.strptime to
# convert it into datetime datatype
datetime_obj = datetime.strptime(datetime_str,
								"%d%b%Y%H%M%S")

# It will print the datetime object
print("date time : {}".format(datetime_obj))

# extract the time from datetime_obj
time = datetime_obj.time()

# it will print time that we
# have extracted from datetime obj
print("Time : {}".format(time))

# extract minute from time
minute = time.minute
print("Minute : {}".format(minute))

# extract second from time
second = time.second
print("Second : {}".format(second))
