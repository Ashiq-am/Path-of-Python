from datetime import datetime
import pytz

# get the standard UTC time
original = pytz.utc

# create datetime object
dateTimeObj = datetime.now(original)
print("Original Date & Time: ",
	dateTimeObj.strftime('%Y:%m:%d %H:%M:%S %Z %z'))

# it will get the time zone
# of the specified location
for timeZone in pytz.all_timezones:
	if 'Indian/' in timeZone:
		dateTimeObj = datetime.now(pytz.timezone(timeZone))
		print(timeZone,":",dateTimeObj.strftime('%Y:%m:%d %H:%M:%S %Z %z'))
