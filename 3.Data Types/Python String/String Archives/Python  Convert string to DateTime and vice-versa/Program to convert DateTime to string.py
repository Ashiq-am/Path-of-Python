import time


# Function to convert string to datetime
def convert(datetime_str):
    datetime_str = time.mktime(datetime_str)

    format = "%b %d %Y %r"  # The format
    dateTime = time.strftime(format, time.gmtime(datetime_str))
    return dateTime


# Driver code
date_time = (2018, 12, 4, 10, 7, 00, 1, 48, 0)
print(convert(date_time))
