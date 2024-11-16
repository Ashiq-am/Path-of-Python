from datetime import datetime
import calendar

# Get current date and time
dt = datetime.today()
seconds = calendar.timegm(dt.utctimetuple())

print(seconds)
