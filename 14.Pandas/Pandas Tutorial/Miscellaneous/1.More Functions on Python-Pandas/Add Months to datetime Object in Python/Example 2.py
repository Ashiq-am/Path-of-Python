# import packages
from datetime import date
from dateutil.relativedelta import relativedelta

# adding months to a particular date
print('date : ' + str(date(2020, 5, 15)))
new_date = date(2020, 5, 15) + relativedelta(months=5)
print('new date is : '+str(new_date))
