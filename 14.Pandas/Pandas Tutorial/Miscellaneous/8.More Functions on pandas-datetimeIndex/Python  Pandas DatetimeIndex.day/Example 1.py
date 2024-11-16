# importing pandas as pd
import pandas as pd

# Create the DatetimeIndex
# Here the 'W' represents Weekly frequency
didx = pd.DatetimeIndex(start ='2014-08-01 10:00', freq ='W',
							periods = 5, tz ='Asia/Calcutta')

# Print the DatetimeIndex
print(didx)
