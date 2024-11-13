from datetime import timezone
import datetime


# Getting the current date
# and time
dt = datetime.datetime.now(timezone.utc)

utc_time = dt.replace(tzinfo=timezone.utc)
utc_timestamp = utc_time.timestamp()

print(utc_timestamp)
