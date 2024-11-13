from datetime import datetime

# Example time string
time_string = "2024-09-26 14:23:45.123"

# Define the format
time_format = "%Y-%m-%d %H:%M:%S.%f"

# Parse the time string into a datetime object
parsed_time = datetime.strptime(time_string, time_format)

# Output the parsed datetime object
print(parsed_time)
print("Year:", parsed_time.year)
print("Month:", parsed_time.month)
print("Day:", parsed_time.day)
print("Hour:", parsed_time.hour)
print("Minute:", parsed_time.minute)
print("Second:", parsed_time.second)
print("Microsecond:", parsed_time.microsecond)
