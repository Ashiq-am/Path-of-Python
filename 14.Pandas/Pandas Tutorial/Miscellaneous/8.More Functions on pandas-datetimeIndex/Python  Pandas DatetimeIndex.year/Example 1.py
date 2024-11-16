# importing pandas as pd
import pandas as pd

# Create the DatetimeIndex
# Here the 'B' represents Business day frequency
didx = pd.DatetimeIndex(start ='2014-08-01 10:00', freq ='B',
							periods = 5, tz ='Asia/Calcutta')

# Print the DatetimeIndex
print(didx)
