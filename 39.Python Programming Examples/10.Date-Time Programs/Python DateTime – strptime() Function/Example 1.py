# import datetime module from datetime
from datetime import datetime

# consider the time stamp in string format
# DD/MM/YY H:M:S.micros
time_data = "25/05/99 02:35:5.523"

# format the string in the given format :
# day/month/year hours/minutes/seconds-micro
# seconds
format_data = "%d/%m/%y %H:%M:%S.%f"

# Using strptime with datetime we will format
# string into datetime
date = datetime.strptime(time_data, format_data)

# display milli second
print(date.microsecond)

# display hour
print(date.hour)

# display minute
print(date.minute)

# display second
print(date.second)

# display date
print(date)
