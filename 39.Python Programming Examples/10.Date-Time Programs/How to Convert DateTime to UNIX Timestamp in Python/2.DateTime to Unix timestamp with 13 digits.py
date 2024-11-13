import time
import datetime

presentDate = datetime.datetime.now()
unix_timestamp = datetime.datetime.timestamp(presentDate)*1000
print(unix_timestamp)
