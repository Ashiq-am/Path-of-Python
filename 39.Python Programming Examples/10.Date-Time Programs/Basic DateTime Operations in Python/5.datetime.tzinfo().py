# code
from datetime import datetime, timedelta
from pytz import timezone
import pytz

time_zone = timezone('Asia/Calcutta')

normal = datetime(2021, 3, 16)
ambiguous = datetime(2021, 4, 16, 23, 30)

# is_dst parameter is ignored for most of the
# timstamps.It is only used during DST
# transition ambiguous periods to resolve that
# ambiguity
print("Operations on normal datetime")
print(time_zone.utcoffset(normal, is_dst=True))
print(time_zone.dst(normal, is_dst=True))
print(time_zone.tzname(normal, is_dst=True))

# put is_dst=False
print(time_zone.utcoffset(normal, is_dst=False))
print(time_zone.dst(normal, is_dst=False))
print(time_zone.tzname(normal, is_dst=False))

print("\n")
print("Opeartions on ambiguous datetime")
print(time_zone.utcoffset(ambiguous, is_dst=True))
print(time_zone.dst(ambiguous, is_dst=True))
print(time_zone.tzname(ambiguous, is_dst=True))

# is_dst=False
print(time_zone.utcoffset(ambiguous, is_dst=False))
print(time_zone.dst(ambiguous, is_dst=False))
print(time_zone.tzname(ambiguous, is_dst=False))
