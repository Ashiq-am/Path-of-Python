# importing pandas as pd
import pandas as pd

# Create the DatetimeIndex
# Here the 'BH' represents business hour frequency
didx = pd.DatetimeIndex(start ='2014-08-01 10:05', freq ='BH',
							periods = 5, tz ='Asia/Calcutta')

# Print the DatetimeIndex
print(didx)
