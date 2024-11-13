# import necessary packages
from datetime import datetime
from dateutil import rrule

# dates
start_date = datetime(2021, 1, 1)
end_date = datetime(2022, 1, 1)

for dt in rrule.rrule(rrule.MONTHLY, dtstart=start_date, until=end_date):
	print(dt)
