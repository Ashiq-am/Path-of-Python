# Python3 code to illustrate the conversion of
# datetime.datetime to excel serial date number

# Importing datetime module
from datetime import datetime
import datetime as dt


def excel_date(date1):

	# Initializing a reference date
	# Note that here date is not 31st Dec but 30th!
	temp = dt.datetime(1899, 12, 30)
	delta = date1 - temp
	return float(delta.days) + (float(delta.seconds) / 86400)


# Calculating the excel serial date number
# for the date "2021-05-04" by calling the
# user defined function excel_date()
print(excel_date(datetime(2021, 2, 4)))
