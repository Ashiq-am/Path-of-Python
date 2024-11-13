# Manipulate DATETIME
from datetime import datetime, timedelta
current = datetime.now()
print("This is the current date and time :- ", current)

# FOR PRINTING TOMORROW'S DATE
tomorrow = timedelta(1)
print("Tomorrow's date and time :- ", current + tomorrow)

# FOR PRINTING YESTERDAY'S DATE
yesterday = timedelta(-1)
print("Yesterday's date and time :- ", current + yesterday)
