# import important module
import datetime
from datetime import datetime

# Create datetime string
datetime_str = "32JAN2022102356"
try:

    # call datetime.strptime to convert it into
    # datetime datatype
    datetime_obj = datetime.strptime(datetime_str,
                                     "%d%b%Y%H%M%S")

    # It will print the datetime object
    print("date time : {}".format(datetime_obj))
except:
    print("You have entered Incorrect Date, please enter a valid date")
