# importing pandas as pd
import pandas as pd

# Create the DatetimeIndex
# Here the 'M' represents Month end frequency
didx = pd.DatetimeIndex(start ='2014-08-01 10:00', freq ='M',
						periods = 5, tz ='Asia/Calcutta')

# Print the DatetimeIndex
print(didx)
