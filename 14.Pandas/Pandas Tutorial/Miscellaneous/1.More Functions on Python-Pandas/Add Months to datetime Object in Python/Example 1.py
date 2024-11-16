# import packages
import numpy as np

# adding months to a given date
print('old date is : ' + str(np.datetime64('2022-04')))
new_date = np.datetime64('2022-04') + np.timedelta64(5, 'M')
print('new date is : '+str(new_date))
