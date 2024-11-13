from datetime import datetime

datetime_string = "15/06/2021 13:30:15.120"

print(type(datetime_string))

format = "%d/%m/%Y %H:%M:%S.%f"

# converting datetime string to datetime
# object with milliseconds..
date_object = datetime.strptime(datetime_string, format)

print("date_object =", date_object)

# Type is datetime object
print(type(date_object))
