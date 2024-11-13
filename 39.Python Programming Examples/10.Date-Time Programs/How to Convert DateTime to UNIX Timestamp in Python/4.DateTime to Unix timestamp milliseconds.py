import datetime
import time

ms = datetime.datetime.now()
print(time.mktime(ms.timetuple()) * 1000)
