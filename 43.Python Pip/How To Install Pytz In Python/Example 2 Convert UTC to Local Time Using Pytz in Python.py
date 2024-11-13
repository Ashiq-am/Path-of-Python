import pytz
from datetime import datetime
import pytz

# Create a time zone-aware datetime object in UTC
utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)

# Convert to a specific time zone (e.g., New York)
local_timezone = pytz.timezone('America/New_York')
local_time = utc_now.astimezone(local_timezone)

print(f'UTC Time: {utc_now}')
print(f'Local Time (New York): {local_time}')
