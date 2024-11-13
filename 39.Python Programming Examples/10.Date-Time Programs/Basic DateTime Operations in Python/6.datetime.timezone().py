from datetime import datetime, timedelta
from pytz import timezone
import pytz

utc = pytz.utc
print(utc.zone)

india = timezone('Asia/Calcutta')
print(india.zone)

eastern = timezone('US/Eastern')
print(eastern.zone)

time_format = '%Y-%m-%d %H:%M:%S %Z%z'

# localize() is used to localize
# datetime with no timezone information
loc_dt = india.localize(datetime(2021, 3, 16, 6, 0, 0))
loc_dt = india.localize(datetime(2021, 3, 16, 6, 0, 0))
print(loc_dt.strftime(time_format))

# another way of building a localized time is by converting
# an existing localized time
# using the standard astimezone() method
eastern_dt = loc_dt.astimezone(eastern)
print(eastern_dt.strftime(time_format))

print(datetime(2021, 3, 16, 12, 0, 0, tzinfo=pytz.utc).strftime(time_format))

# 10 minutes before
before_dt = loc_dt - timedelta(minutes=10)
print(before_dt.strftime(time_format))
print(india.normalize(before_dt).strftime(time_format))

# 20 mins later
after_dt = india.normalize(before_dt + timedelta(minutes=20))
print(after_dt.strftime(time_format))
