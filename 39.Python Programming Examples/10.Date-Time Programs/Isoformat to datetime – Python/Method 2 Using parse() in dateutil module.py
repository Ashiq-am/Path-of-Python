# importing datetime module
from datetime import datetime
import dateutil

# Getting today's date
todays_Date = datetime.now()
isoformat_date = todays_Date.isoformat()

# display isoformat type
print(type(isoformat_date))

# convert it into datetime and display
result = dateutil.parser.parse(isoformat_date)
print(type(result))
