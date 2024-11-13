from datetime import datetime
import pytz

# get the standard UTC time
original = pytz.timezone('Asia/Kolkata')

# it will get the time zone
# of the specified location
converted = pytz.timezone('US/Eastern')

# print the date and time in
# specified format
dateTimeObj = datetime.now(original)
print("Original Date & Time: ",
	dateTimeObj.strftime('%Y:%m:%d %H:%M:%S %Z %z'))

# converted
dateTimeObj = datetime.now(converted )
print("Converted Date & Time: ",
	dateTimeObj.strftime('%Y:%m:%d %H:%M:%S %Z %z'))
