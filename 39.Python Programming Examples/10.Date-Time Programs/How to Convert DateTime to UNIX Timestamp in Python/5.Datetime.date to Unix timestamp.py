import datetime
import time

datetime = datetime.date(2021, 8, 6)
print("Unix_Time: ",
	(time.mktime(datetime.timetuple())))
