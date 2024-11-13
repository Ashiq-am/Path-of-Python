from datetime import datetime, timezone

# Create a datetime object
dt = datetime(2024, 1, 25, 12, 0, 0)

# Convert to UTC timestamp using timestamp() method
timestamp_utc = dt.replace(tzinfo=timezone.utc).timestamp()

print("Datetime:",dt)
print("UTC Timestamp:", timestamp_utc)
