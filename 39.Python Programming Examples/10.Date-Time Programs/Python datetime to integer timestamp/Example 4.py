import datetime
import pytz

dtime = datetime.datetime.now()
timezone = pytz.timezone("Asia/Kolkata")
dtzone = timezone.localize(dtime)

print("Time Zone: ", dtzone.tzinfo)
print("Datetime: ", dtzone)

tstamp = dtzone.timestamp()
print("Integer timestamp: ", int(round(tstamp)))
