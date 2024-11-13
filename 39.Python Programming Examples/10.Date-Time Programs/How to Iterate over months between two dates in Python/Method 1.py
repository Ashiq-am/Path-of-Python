# import necessary packages
from datetime import datetime, timedelta

# date initilaisation
startDate = datetime(2020, 1, 10)
endDate = datetime(2020, 4, 20)

# stores 31 days that can be added
addDays = timedelta(days=31)

while startDate <= endDate:
	print(startDate)
	# add a month
	startDate += addDays
