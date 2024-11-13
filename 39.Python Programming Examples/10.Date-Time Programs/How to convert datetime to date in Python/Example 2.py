# import important module
import datetime
from datetime import datetime

# Create datetime string
datetime_str = "100201095407"
print("datetime string : {}".format(datetime_str))

# call datetime.strptime to convert
# it into datetime datatype
datetime_obj = datetime.strptime(datetime_str,
								"%d%m%y%H%M%S")

# It will print the datetime object
print(datetime_obj)

# extract the time from datetime_obj
date = datetime_obj.date()

# it will print date that we have
# extracted from datetime obj
print(date)
