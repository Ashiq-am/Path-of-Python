import calendar
from datetime import datetime

# Create a datetime object
dt = datetime(2024, 1, 25, 12, 0, 0)

# Convert to UTC timestamp using timegm() function
timestamp_utc = calendar.timegm(dt.utctimetuple())

print("Datetime:", dt)
print("UTC Timestamp:", timestamp_utc)
