import time
from datetime import datetime

# Create a datetime object
dt = datetime(2024, 1, 25, 12, 0, 0)

# Convert to UTC timestamp using time.mktime
timestamp_utc = int(time.mktime(dt.timetuple()))

print("Datetime:", dt)
print("UTC Timestamp:", timestamp_utc)
