# import packages
import pandas as pd

# adding months to a particular date
present = '2022-05-05'
print('date : ' + present)
new_date = pd.to_datetime(present)+pd.DateOffset(months=5)
print('new date is : '+str(new_date))
