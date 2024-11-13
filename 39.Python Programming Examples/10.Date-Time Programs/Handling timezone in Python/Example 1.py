import datetime
import pytz

dtObject_local = datetime.datetime.now()
dtObject_utc = datetime.datetime.now(pytz.utc)

print(dtObject_local)
print(dtObject_utc)
