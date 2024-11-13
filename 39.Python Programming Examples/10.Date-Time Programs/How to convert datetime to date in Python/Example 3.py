# import important module
from datetime import datetime

# call datetime.strptime to
# convert it into datetime datatype
datetime_obj = datetime.now()

# It will print the datetime object
print(datetime_obj)

# extract the time from datetime_obj
date = datetime_obj.date()
print(date)
