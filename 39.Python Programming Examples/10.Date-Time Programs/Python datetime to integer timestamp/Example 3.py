import datetime
import calendar

d = datetime.datetime(1970, 1, 1, 2, 1, 0)
ttuple = d.timetuple()

itimestamp = calendar.timegm(ttuple)
print("Timestamp in integer since epoch:",
	itimestamp)
