from datetime import datetime, timedelta

# adding 9 hours
hour_delta = timedelta(hours=9)

# Storing the new date
timeAdded = datetime.now() + hour_delta

# Displaying current date and time with
# adding 9 hours
print(f"The date after adding 9 hours: {timeAdded}")

# adding 1 day
day_delta = timedelta(days=1)

# storing the new date
dateAdded = datetime.now() + day_delta

# Displaying current date and time with
# adding 1 day
print(f"The date after adding 1 day: {dateAdded}")
