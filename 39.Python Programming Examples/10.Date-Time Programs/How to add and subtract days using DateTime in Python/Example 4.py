# MANIPULATING DATETIME
from datetime import datetime, timedelta

curr = datetime.now()
print("Current Date and time :- ", curr)

new_datetime = timedelta(days = 10, seconds = 40,
						microseconds = 10,
						milliseconds = 60,
						minutes = 10, hours = 4,
						weeks = 8)

print("New Date and time :- ", curr + new_datetime)
