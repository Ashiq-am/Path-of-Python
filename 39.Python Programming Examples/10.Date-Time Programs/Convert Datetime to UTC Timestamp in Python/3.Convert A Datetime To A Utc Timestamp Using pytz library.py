import pytz
from datetime import datetime

# Create a datetime object
dt = datetime(2024, 1, 25, 12, 0, 0)

# Set the timezone to UTC
dt_utc = pytz.utc.localize(dt)

# Convert to UTC timestamp
timestamp_utc = int(dt_utc.timestamp())

print("Datetime:", dt)
print("UTC Timestamp:", timestamp_utc)
