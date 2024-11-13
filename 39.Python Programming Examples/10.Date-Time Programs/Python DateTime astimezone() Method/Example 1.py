# Python3 code for getting
# a datetime instance according
# to the specified time zone parameter tz

# Importing datetime module
import datetime

# Specifing Singapore timedelta and timezone
# object
sgtTimeDelta = datetime.timedelta(hours=5)
sgtTZObject = datetime.timezone(sgtTimeDelta,
								name="SGT")

# Specifing a datetime along with Singapore
# timezone object
d1 = datetime.datetime(2021, 8, 4, 10,
					00, 00, 00, sgtTZObject)

# Calling the astimezone() function over the above
# specified Singapore timezone
d2 = d1.astimezone(sgtTZObject)

# Printing a datetime instance as per the above
# specified Singapore timezone
print("Singapore time from a datetime instance:{}".format(d2))
